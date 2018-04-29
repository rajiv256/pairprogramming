from django.db import models


class User(models.Model):

    user_name         = models.CharField(max_length=100)
    user_email        = models.EmailField()
    user_about        = models.TextField(max_length=500)
    user_github_token = models.CharField(max_length=500)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ('user_name',)


class Post(models.Model):
    post_owner      = models.ForeignKey(User, related_name='my_posts', on_delete=models.CASCADE)
    post_pub        = models.DateTimeField('date published')
    post_title      = models.CharField(max_length=100)
    post_content    = models.TextField(max_length=1000)
    post_interested = models.ManyToManyField(User)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ('-post_pub',)


class Repo(models.Model):
    repo_name        = models.CharField(max_length=100)
    repo_url         = models.URLField(max_length=500)
    repo_owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_repos')
    repo_members     = models.ManyToManyField(User)
    repo_forks       = models.PositiveIntegerField(default=0)
    repo_stars       = models.PositiveIntegerField(default=0)
    repo_description = models.TextField(max_length=500)
    repo_pub         = models.DateTimeField()

    class Meta:
        ordering = ('-repo_forks','-repo_stars','-repo_pub',)

