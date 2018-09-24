from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login


def home_page(request):
    return render(request,"home_page.html",{})

def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated())
    if(form.is_valid()):
        print(form.cleaned_data)
    context = {
        "form": form
    }
    return render(request,"auth/login.html",context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    print(request.user.is_authenticated())
    if(form.is_valid()):
        print(form.cleaned_data)
    return render(request,"auth/register.html",{})


def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title": "Contact",
        "content": "Welcome to the contact us page",
        "form": contact_form
    }