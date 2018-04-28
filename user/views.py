from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from user.models import User
from django.http import HttpResponse, HttpResponseRedirect
from github import Github
from user.utils import *





def index(request,user_name):
    repos = []
    context = {
        'user_name': user_name,
        'repos': repos,
    }
    return render(request, 'user/user_profile.html', context)


def signinForm(request):
    return render(request, 'signin.html', None)


def signin(request):
    login_user(request.POST['user_name'], request.POST['password'])
    return HttpResponseRedirect(reverse('user:profile', args=(request.POST['user_name'],)))
