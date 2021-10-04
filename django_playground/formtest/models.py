from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile_Info(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_Personnal_site_url = models.URLField(blank=True)
    Profile_Picture = models.ImageField(upload_to = 'Profile_picture',blank=True)
    