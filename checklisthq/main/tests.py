"""
Unit tests for forms and views. See tests in models.py for ORM related tests.
"""
import unittest

from django.contrib.auth.models import User
from django.test.client import Client

from forms import ChecklistForm
from models import Checklist

class TestChecklistForm(unittest.TestCase):
    """
    Ensures the correct behaviour of the form used for editing checklists.
    """

    def test_META(self):
        """
        Simple sanity checks to ensure it's set up correctly.
        """
        self.assertEqual(Checklist, ChecklistForm.Meta.model)
        self.assertEqual(('title', 'content', 'tags'),
            ChecklistForm.Meta.fields)

class TestSearch(unittest.TestCase):
    """
    Ensures the correct behaviour of the form used for editing checklists.
    """

    def setUp(self):
        self.user,_ = User.objects.get_or_create(username="test_user")
        self.cl1 = Checklist(title='foo', owner=self.user, content='bar')
        self.cl1.save()
        self.cl1.tags.add("foo")

        self.cl2 = Checklist(title='bar', owner=self.user, content='vavavoom')
        self.cl2.save()
        self.cl2.tags.add("foo")

        self.cl2 = Checklist(title='bar', owner=self.user, content='vavavoom')
        self.cl2.save()
        self.cl2.tags.add("bar")


    def test_duplicates(self):
        """
        Test for issue #53.
        Search Function returns two instances of the same checklist if
        a term is used both in the title and in the tag.
        """
        c = Client()
        response = c.get('/search', {'query': 'foo'})
        # Just count TRs for now to get the results.
        self.assertEqual( response.content.count("<tr "), 2)




