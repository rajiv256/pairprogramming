from django.urls import path
from topic import views


app_name = 'topic'
urlpatterns = [
    path('<topic_name>/', views.index, name='index'),
]