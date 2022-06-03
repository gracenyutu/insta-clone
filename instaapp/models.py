from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='user')
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings")
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(null=False, default='default.jpg')
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    likes = models.CharField(max_length=100, null=False, blank=False)
    comments = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.caption
