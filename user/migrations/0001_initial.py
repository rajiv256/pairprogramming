# Generated by Django 2.0.4 on 2018-05-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_title', models.CharField(default='my awesome idea', max_length=100)),
                ('idea_description', models.TextField(default='my awesome idea', max_length=500)),
                ('idea_upvotes', models.PositiveIntegerField(default=0)),
                ('idea_downvotes', models.PositiveIntegerField(default=0)),
                ('idea_status', models.IntegerField(choices=[(0, 'CLOSED'), (1, 'OPEN')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='plouhc', max_length=100)),
                ('user_email', models.EmailField(default='rajivpensidpri@gmail.com', max_length=254)),
                ('user_about', models.TextField(default='ab', max_length=500)),
                ('user_github_token', models.CharField(default='abb', max_length=500)),
                ('user_followers', models.PositiveIntegerField(default=0)),
                ('user_relationships', models.ManyToManyField(related_name='related_to', through='user.Relationship', to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_followers',
            field=models.ManyToManyField(blank=True, related_name='interested_areas', to='user.User'),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_ideas',
            field=models.ManyToManyField(blank=True, related_name='related_topics', to='user.Idea'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_relationships', to='user.User'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_relationships', to='user.User'),
        ),
        migrations.AddField(
            model_name='idea',
            name='idea_interested_users',
            field=models.ManyToManyField(blank=True, to='user.User'),
        ),
        migrations.AddField(
            model_name='idea',
            name='idea_owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_ideas', to='user.User'),
        ),
    ]
