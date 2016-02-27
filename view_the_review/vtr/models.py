from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    rollnumber = models.PositiveIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    branch = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Query(models.Model):
    title = models.CharField(max_length=100, default='title')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    # setting blank true we indicate that field is not required and can be left blank null true allow blank values to be stored in db as Null.
    views = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Query, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
