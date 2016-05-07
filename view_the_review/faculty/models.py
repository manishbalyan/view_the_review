"""Imports for faculty models."""
from django.contrib.auth.models import User
from django.db import models
from vtr.models import upload_to
import datetime


class UserProfileF(models.Model):
    """User profile table for faculty."""

    user = models.OneToOneField(User)
    faculty_id = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True, )
    activation_key = models.CharField(max_length=40, blank=True, null=True)
    key_expires = models.DateTimeField(default=datetime.date.today(), null=True)

    def __unicode__(self):
        """Unicode define UserProfileF."""
        return self.user.username

    class Meta:
        """It describe the user profilr for faculty."""

        verbose_name_plural = u'User profiles'
