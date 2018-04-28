from django.db import models


class User(models.Model):

    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_about = models.TextField(max_length=1000)
    user_github_key = models.CharField(max_length=1000)








