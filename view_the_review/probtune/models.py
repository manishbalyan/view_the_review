# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from vtr.models import upload_to
from taggit.managers import TaggableManager
from django_comments.models import Comment
from django.contrib.contenttypes import generic
import datetime


class QueryP(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    show_user = models.BooleanField(default=0, null=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    user = models.ForeignKey(User, null=True)
    slug = models.SlugField(unique=True)
    tags = TaggableManager()
    comments = generic.GenericRelation(Comment, object_id_field="object_pk")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(QueryP, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
