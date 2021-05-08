from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
def userLogin(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == "POST":
        formData = LoginForm(request.POST)
        if formData.is_valid():
            user = authenticate(request, username= formData.cleaned_data['username'], password= formData.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('/home')
            else:
                messages.warning(request, "Invalid Login Credentials")
                return redirect('/authentication/authenticate.do/')
        else:
            context['form'] = formData
            return render(request, 'authentication/login.html', context)
    else:
        context['form'] = LoginForm(None)
        return render(request, 'authentication/login.html', context)

def userSignUp(request):
    context = {}
    if request.method == "POST":
        formData = SignUpForm(request.POST)
        if formData.is_valid():
            username = formData.cleaned_data['username']
            first_name = formData.cleaned_data['name']
            email = formData.cleaned_data['email']
            password = formData.cleaned_data['password']
            try:
                User.objects.get(username = username, password= password)
                messages.warning(request, "User already Registered")
                return redirect('/authentication/authenticate.do/')
            except ObjectDoesNotExist:
                user = User.objects.create_user(username= username, email= email, first_name= first_name, password= password)
                messages.success(request, "Signed Up Successfully")
                return redirect('/authentication/authenticate.do/')
        else:
            context['form'] = formData
            return render(request, 'authentication/signup.html', context)
    else:
        context['form'] = SignUpForm(None)
        return render(request, 'authentication/signup.html', context)

def userLogout(request):
    logout(request)
    return redirect('/home') 
