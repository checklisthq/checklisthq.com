"""
Unit tests for forms and views. See tests in models.py for ORM related tests.
"""
import unittest

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
