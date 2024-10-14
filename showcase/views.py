f# showcase/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

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
            form.save()
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'showcase/contact.html', {'form': form})

