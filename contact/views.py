from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


# Create your views here.


def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #everithing was ok
            return redirect(reverse('contact')+"?ok")
    return render(request, "contact/contact.html", {"form": contactForm})

