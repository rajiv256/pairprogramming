from django.urls import path
from user import views


app_name = 'user'
urlpatterns = [
    path('<user_name>/', views.index, name='profile'),
]