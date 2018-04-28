from django.shortcuts import render
from django.views import generic
from user.models import User
from django.http import HttpResponse, HttpResponseRedirect


'''
class IndexView(generic.DetailView):

    model = User
    template_name = 'user/user_profile.html'

    def get_queryset(self):
        return None 

'''
def index(request):
    context = {
        'user_name' : 'rajiv256',
    }
    return render(request, 'user/user_profile.html', context)
