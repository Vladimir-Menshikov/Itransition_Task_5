from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.models import User 
from . import funcs

def home(request):
    if request.method == 'POST':
        ids = request.POST.getlist('id')
        if 'block' in request.POST:
            funcs.block(ids)
        elif 'unblock' in request.POST:
            funcs.unblock(ids)
        elif 'delete' in request.POST:
            funcs.delete(ids)
    users = User.objects.all()
    return render(request,'app/index.html',{'users': users})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})