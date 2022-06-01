from django.db import models

# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(null=False, default='default.jpg')

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
