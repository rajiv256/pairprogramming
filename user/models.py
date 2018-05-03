from django.db import models
from .choices import IDEA_STATUS
import random


RELATIONSHIP_FOLLOWING      = 1
RELATIONSHIP_BLOCKED        = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, "Following"),
    (RELATIONSHIP_BLOCKED, 'Blocked')
)


class User(models.Model):

    user_name            = models.CharField(max_length=100, default=''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6)))
    user_email           = models.EmailField(default='rajivpensidpri@gmail.com')
    user_about           = models.TextField(max_length=500, default='ab')
    user_github_token    = models.CharField(max_length=500,default='abb')
    user_relationships   = models.ManyToManyField('self', related_name='related_to', symmetrical=False, through='Relationship')
    user_followers       = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user_name

    def add_relationship(self, user, status):
        relationship, created = Relationship.objects.get_or_create(
            from_user = self,
            to_user   = user,
            status    = status
        )
        return relationship

    def remove_relationship(self, user, status):
        Relationship.objects.filter(
            from_user = self,
            to_user   = user,
            status    = status
        ).delete()
        return

    def get_relationships(self, status):
        return self.user_relationships.filter(
            to_relationships__status=status,
            to_relationships__from_user=self
        )

    def get_related_to(self, status):
        return self.related_to.filter(
            from_relationships__status=status,
            from_relationships__to_user=self
        )

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)


class Relationship(models.Model):

    # user.from_relationships --> Gives all the relationships that emerge from user--> AnotherUser
    from_user = models.ForeignKey(User, related_name='from_relationships', on_delete=models.CASCADE)

    # user.to_relationships --> Gives all the relationships that end in user. AnotherUser --> user
    to_user   = models.ForeignKey(User, related_name='to_relationships', on_delete=models.CASCADE)

    status    = models.IntegerField(choices=RELATIONSHIP_STATUSES)


class Idea(models.Model):
    idea_title            = models.CharField(max_length=100, default='my awesome idea')
    idea_description      = models.TextField(max_length=500, default='my awesome idea')
    idea_owner            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_ideas', blank=True)
    idea_interested_users = models.ManyToManyField(User, blank=True)
    idea_upvotes          = models.PositiveIntegerField(default=0)
    idea_downvotes        = models.PositiveIntegerField(default=0)
    idea_status           = models.IntegerField(choices=IDEA_STATUS, default=1)


# class Repo(models.Model):
#     repo_name        = models.CharField(max_length=100)
#     repo_url         = models.URLField(max_length=500)
#     repo_owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_repos')
#     repo_members     = models.ManyToManyField(User)
#     repo_forks       = models.PositiveIntegerField(default=0)
#     repo_stars       = models.PositiveIntegerField(default=0)
#     repo_description = models.TextField(max_length=500)
#     repo_pub         = models.DateTimeField()


class Topic(models.Model):
    topic_title = models.CharField(max_length=100)
    topic_ideas = models.ManyToManyField(Idea, related_name='related_topics', blank=True)
    topic_followers = models.ManyToManyField(User, related_name='interested_areas', blank=True)
