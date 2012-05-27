from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Checklist(models.Model):
    title = models.CharField(max_length=512)
    owner = models.ForeignKey(User)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True,auto_now_add=True)
    deleted = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    # To add: type

    def __unicode__(self):
        return self.title
