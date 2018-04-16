from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=100)
    creationdate = models.DateTimeField('date created')
    status = models.BooleanField()

class Idea(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    upvotecount = models.IntegerField

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
