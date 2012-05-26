from django.db import models
from django.contrib import auth

class Checklist(models.Model):
    title = models.CharField(max_length=512)
    owner = models.ForeignKey(auth.models.User)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True,auto_now_add=True)
    # To add: tags, type
