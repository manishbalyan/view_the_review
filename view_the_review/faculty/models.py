from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from vtr.models import upload_to

#Create your models here.
class UserProfileF(models.Model):
    user = models.OneToOneField(User)
    faculty_id = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True, default='images/@@@@.jpg')
    
    def __unicode__(self):
        return self.user.username