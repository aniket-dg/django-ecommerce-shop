from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
def userLogin(request):
    context = {}
    if request.method == "POST":
        formData = LoginForm(request.POST)
        if formData.is_valid():
            return redirect('login.done')
        else:
            context['form'] = formData
            return render(request, 'authentication/login.html', context)
    else:
        context['form'] = LoginForm(None)
        return render(request, 'authentication/login.html', context)
