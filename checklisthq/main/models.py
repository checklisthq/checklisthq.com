import unittest

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Checklist(models.Model):
    title = models.CharField(max_length=512)
    owner = models.ForeignKey(User)
    description = models.TextField(default="")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    deleted = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

class TestChecklist(unittest.TestCase):
    """
    Ensures the Checklist class works as expected.
    """

    def test_unicode(self):
        """
        The checklist's title is always returned.
        """
        u = User(username='user1', password='password')
        cl = Checklist(title='foo', owner=u, content='bar')
        self.assertEqual(u'foo', cl.__unicode__())
