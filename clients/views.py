from django.shortcuts import render, redirect, get_object_or_404
from clients.models import Profile, RecentlyViewed
from clients.forms.profile_form import *
from properties.models import Properties
from datetime import datetime
from django.contrib import messages


def register(request):
	if request.method == 'POST':
		regForm = RegisterForm(data=request.POST)
		proForm = fnameRegisterForm(data=request.POST)
		if regForm.is_valid() and proForm.is_valid():
			user = regForm.save()
			profile = proForm.save(commit=False)
			profile.user = user
			profile.save()
			messages.success(request, 'Profile created successfully')
			return redirect('clients-login')
		else:
			messages.error(request, 'Registration failed. Please try again.')
	return render(request, 'clients/register.html', {
		'form': RegisterForm(),
		'fname': fnameRegisterForm()
	})


def profile(request):
    is_agent = request.user.groups.filter(name="agents").exists()
    if request.user.is_authenticated and is_agent is False:
        profile = Profile.objects.filter(user=request.user).first()
        if request.method == 'POST':
            form = ProfileForm(instance=profile, data=request.POST)
            profile = form.save(commit=False)
            profile.user = request.user
            if form.is_valid():
                profile.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('clients-profile')
            else:
                messages.error(request, 'Update failed. Please try again.')
        return render(request, 'clients/profile.html', {
            'form': ProfileForm(instance=profile)
        })
    else:
        return render(request, 'clients/profile.html', {
            'is_agent': is_agent
        })


def get_recently_viewed(request):
	is_agent = request.user.groups.filter(name="agents").exists()
	if request.user.is_authenticated and is_agent is False:
		the_user = Profile.objects.filter(user=request.user).first()
		recently_viewed_obj = RecentlyViewed.objects.filter(user=the_user).order_by('-time')
		if len(recently_viewed_obj) > 0:
			return render(request, 'clients/recently_viewed.html', {
				'recently_viewed': recently_viewed_obj
			})
		else:
			message = 'No previous history to show'
	else:
		message = 'This feature is only available for logged in users'
	context = {
		'message': message,
		'is_agent': is_agent
	}
	return render(request, 'clients/recently_viewed.html', context)



def add_to_recently_viewed(request, the_id):
	is_agent = request.user.groups.filter(name="agents").exists()
	if request.user.is_authenticated and is_agent is False:
		the_user = Profile.objects.filter(user=request.user).first()
		prop = get_object_or_404(Properties, pk=the_id)
		this_user_recent_list = RecentlyViewed.objects.filter(user=the_user)
		print(len(this_user_recent_list))
		entry = this_user_recent_list.filter(property=prop)
		if len(entry) != 0:
			print("the entry ", entry)
			the_entry = entry.first()
			print("entry time, old:", the_entry.time)
			the_entry.time = datetime.now()
			the_entry.save()
			print("the entry time now:", the_entry.time)

		else:
			if len(this_user_recent_list) >= 10:
				oldest = this_user_recent_list[0]
				RecentlyViewed.objects.filter(id=oldest.id).delete()
			form = RecentlyViewedForm(data=request.POST)
			recently_viewed = form.save(commit=False)
			recently_viewed.user = the_user
			recently_viewed.property = prop
			if form.is_valid():
				recently_viewed.save()
				print(recently_viewed)

			"""if len(this_user_recent_list) == 10:
				oldest = this_user_recent_list[0]
				RecentlyViewed.objects.filter(id=oldest.id).delete()"""
