# showcase/views.py
import json
import requests
import os
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings


def home(request):
    return render(request, 'showcase/home.html')

def services(request):
    return render(request, 'showcase/services.html')

def portfolio(request):
    return render(request, 'showcase/portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save the contact message to the database
            form.save()

            # Prepare email details
            subject = f"New message from {form.cleaned_data['name']}"
            message_body = f"Message: {form.cleaned_data['message']}\nFrom: {form.cleaned_data['email']}"

            # Send email
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [os.getenv('EMAIL_RECIPIENT')],  # Replace with your email or environment variable
                fail_silently=False,
            )

            # Show success message
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'showcase/contact.html', {'form': form})
