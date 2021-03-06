from django.shortcuts import render, get_object_or_404
from agents.models import Agents
from properties.models import Properties
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from agents.forms.send_email import ContactForm


def about(request):
    is_agent = request.user.groups.filter(name="agents").exists()
    context = {
        'agents': Agents.objects.all(),
        'is_agent': is_agent
    }
    return render(request, 'about.html', context)


def get_agent_by_id(request, id):
    is_agent = request.user.groups.filter(name="agents").exists()
    return render(request, 'agents/agent_details.html', {
        'agent': get_object_or_404(Agents, pk=id),
        'properties': Properties.objects.filter(agent=id),
        'agents': Agents.objects.exclude(id=id),
        'is_agent': is_agent
    })


def contact(request):
    is_agent = request.user.groups.filter(name="agents").exists()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['castle_apartments@hotmail.com'])
                messages.success(request, 'Success, email sent')
            except BadHeaderError:
                messages.error(request, "Something went wrong, email wasn't sent")
    return render(request, 'contact.html', {
        'form': ContactForm(),
        'is_agent': is_agent
    })
