from django.db import models


class User(models.Model):

    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_about = models.TextField(max_length=1000)
    user_github_token = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ('user_name',)


class Post(models.Model):
    post_owner = models.ForeignKey(User, related_name='my_posts', on_delete=models.CASCADE)
    post_pub   = models.DateTimeField('date published')
    post_title = models.CharField(max_length=50)
    post_content = models.TextField(max_length=1000)
    post_interested = models.ManyToManyField(User)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ('-post_pub',)



