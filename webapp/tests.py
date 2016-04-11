# Core Django imports
from django.test import TestCase
from django.contrib.auth.models import User
from webapp.forms import *
from django.utils import timezone

# Imports from my apps
from webapp.models import *

# Create your tests here.


class IssueFormTest(TestCase):

    fixtures = [
        'webapp_test_users.json'
    ]

    def setUp(self):
        self.user = User.objects.get(id=1)
        self.valid_data = {
            'title': 'Testing Title',
            'type': Issue.TYPE_BUG,
            'summary': 'This is the testing summary',
            'date_registered': timezone.now(),
            'is_solved': False
        }

    def test_filled_form_is_valid(self):
        form = IssueForm(self.user, self.valid_data)
        self.assertTrue(form.is_valid(), "error are" + form.errors.as_text())
