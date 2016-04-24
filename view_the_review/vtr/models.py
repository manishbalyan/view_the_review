from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django_comments.models import Comment
from django.contrib.contenttypes import generic
import os
import uuid
from taggit.managers import TaggableManager
import datetime



def upload_to(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('images', filename)


# Create your models here.


class UserProfileS(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    rollnumber = models.PositiveIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    branch = models.CharField(max_length=30, blank=True, null=True)
    hostler = models.BooleanField(default=0)
    profile_pic = models.ImageField(upload_to="images", blank=True, null=True, default='images/@@@@.jpg')
    activation_key = models.CharField(max_length=40, blank=True, null=True)
    key_expires = models.DateTimeField(default=datetime.date.today(), null=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'


class QueryS(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True)
    show_user = models.BooleanField(default=0, null=False)
    branch = models.CharField(max_length=20, blank=True, null=True)
    views = models.IntegerField(default=0)
    #votes = models.ManyToManyField(User, related_name='votess')
    #abuses = models.ManyToManyField(User, related_name='abusess')
    user = models.ForeignKey(User, null=True)
    slug = models.SlugField(unique=True)
    tags = TaggableManager(related_name='tags')
    comments = generic.GenericRelation(Comment, object_id_field="object_pk")

    @property
    def total_votes(self):
        return self.votess.count()

    @property
    def total_abuses(self):
        return self.abusess.count()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(QueryS, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Thread(models.Model):
    # ...
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='threadUpVotes')
    userDownVotes = models.ManyToManyField(User, blank=True, related_name='threadDownVotes')