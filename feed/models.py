from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):

    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

