from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from user.models import User, Idea
from django.http import HttpResponse, HttpResponseRedirect
from github import Github
from user.utils import *


def index(request, user_name):
    ideas = Idea.objects.filter(idea_owner__user_name__contains='rajiv')
    context = {
        'user_name': user_name,
        'ideas'    : ideas,
    }
    return render(request, 'user/profile.html', context)


def signinForm(request):
    return render(request, 'signin.html', None)


def signin(request):
    request.session['user_name'] = request.POST['user_name']
    login_user(request.POST['user_name'], request.POST['password'])
    return HttpResponseRedirect(reverse('user:profile', args=(request.POST['user_name'],)))


def mystory(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/mystory.html', context)


def feed(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/feed.html', context)


def timeline(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/timeline.html', context)


def projects(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/projects.html', context)


def following(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/following.html', context)


def followers(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'user/followers.html', context)
