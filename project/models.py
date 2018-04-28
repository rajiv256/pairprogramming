from django.db import models
from user.models import User


class Project(models.Model):

    project_title = models.CharField(max_length=20)
    project_summary = models.CharField(max_length=1000)
    project_owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    project_members = models.ManyToManyField(User)
    project_pub = models.DateTimeField('date created')

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ('-project_pub', )
