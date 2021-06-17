from django.db import models
from django.conf import settings
from accounts.models import Profile
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
