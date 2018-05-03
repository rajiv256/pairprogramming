from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from user.models import User, Idea
from user.models import Topic
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from github import Github
from user.utils import *
from dal import autocomplete


class TopicAutoComplete(autocomplete.Select2QuerySetView):
    #TODO : Don't forget to add proper permission checks to the querying user.
    def get_queryset(self):

        qs = Topic.objects.all()
        if self.q:
            qs = qs.filter(topic_title__isstartswith=self.q)
        return qs[:10]


def autocomplete(request):
    topics = Topic.objects.all()
    tags = [t.topic_title for t in topics]
    return JsonResponse(list(set(tags))[:3000], safe=False)


def index(request, user_name):
    add_all_topics()
    topics = Topic.objects.all()
    print(topics.count())
    context = {
        'user_name': user_name,
        'topics'    : topics,
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

