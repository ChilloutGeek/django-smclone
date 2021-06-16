from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=350, default='welcome to my bio', null=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    
    def __str__(self):
        return str(self.user)
        
    def profiles_post(self):
        return self.post_set.all()
