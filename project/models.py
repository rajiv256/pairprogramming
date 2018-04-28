from django.db import models
from user.models import User


class Project(models.Model):

    project_title = models.CharField(max_length=20)
    project_summary = models.TextField(max_length=1000)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)

