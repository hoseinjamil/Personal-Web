from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMe
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import ContactMe
from django.contrib import messages


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Create ContactMe object
        ContactMe.objects.create(name=name, email=email, subject=subject, body=body)
        messages.success(request, 'Your message was sent successfully.')
        return redirect('contact')  # Redirect to the contact page after successful form submission

    return render(request, 'home/index.html', {})


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Create ContactMe object
        ContactMe.objects.create(name=name, email=email, subject=subject, body=body)
        messages.success(request, 'Your message was sent successfully.')
        return redirect('contact')  # Redirect to the contact page after successful form submission

    return render(request, 'home/index.html', {})
