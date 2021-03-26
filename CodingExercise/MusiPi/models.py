from django.db import models
from django_mysql.models import ListCharField

# Create your models here.


class Song(models.Model):
    songName = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploadedTime = models.DateTimeField(auto_now=True)


class Podcast(models.Model):
    podcastName = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploadedTime = models.DateTimeField(auto_now=True)
    hostName = models.CharField(max_length=100)
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10*101),
        default=""
    )


class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploadedTime = models.DateTimeField(auto_now=True)
