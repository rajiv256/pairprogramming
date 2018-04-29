from django.contrib import admin
from .models import User, Repo


admin.site.register(User, Repo)
