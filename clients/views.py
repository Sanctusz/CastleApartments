from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from clients.models import Profile, RecentlyViewed
from clients.forms.profile_form import ProfileForm
from properties.models import Properties
from datetime import datetime


# Create your views here.
def index(request):
	return render(request, 'clients/index.html')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('clients-login')
	return render(request, 'clients/register.html', {
		'form': UserCreationForm()
	})


def profile(request):
	profile = Profile.objects.filter(user=request.user).first()
	if request.method == 'POST':
		form = ProfileForm(instance=profile, data=request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('clients-profile')
	return render(request, 'clients/profile.html', {
		'form': ProfileForm(instance=profile)
	})


def get_recently_viewed(request):
	the_user = request.user
	return RecentlyViewed.objects.filter(user=the_user).order_by(datetime)


def add_to_recently_viewed(request,id):
	# ToDo Finish!!!!
	the_id = id
	the_user = request.user
	prop = Properties.objects.filter(id=the_id)
	if (the_user.groups.filter(name='clients').exists()):
		this_user_recent_list = get_recently_viewed(request)
		the_entry = this_user_recent_list.filter(property_id=the_id)
		if the_entry is not None:
			the_entry.time = datetime.now
		else:
			obj = RecentlyViewed(the_user, prop, datetime.now)
			if len(this_user_recent_list) == 10:
				oldest = this_user_recent_list[0]
				RecentlyViewed.objects.filter(id=oldest.id).delete()
			obj.save()
			RecentlyViewed.save()
