from django.urls import path
from user import views


app_name = 'user'
urlpatterns = [
    path('<user_name>/', views.index, name='profile'),
    path('<user_name>/feed/', views.feed, name='feed'),
    path('<user_name>/projects/', views.projects, name='projects'),
    path('<user_name>/timeline/', views.timeline, name='timeline'),
    path('<user_name>/mystory/', views.mystory, name='mystory'),
    path('<user_name>/following/', views.following, name='following'),
    path('<user_name>/followers/', views.followers, name='followers'),
]
