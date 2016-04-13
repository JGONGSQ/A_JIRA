# Core Django imports
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone


# Imports from apps
from .models import Issue as Model_Issue
from .forms import IssueForm
from webapp.views import create_issue_jira

# Imports from Python calls
import unittest
import mock
import sys, os
# from jira import JIRA
import json

# Create your tests here.


class IssueFormTest(TestCase):

    # define some defaults data in the json file
    fixtures = [
        'webapp_test_users.json'
    ]

    # setup some defaults data for this test
    def setUp(self):
        self.user = User.objects.get(id=1)
        self.valid_data = {
            'title': 'Testing Title',
            'type': Model_Issue.TYPE_BUG,
            'summary': 'This is the testing summary',
            'date_registered': timezone.now(),
            'is_solved': False
        }

    # test the issue form with valid data
    def test_form_filled_with_valid_data_is_valid(self):
        form = IssueForm(self.user, self.valid_data)
        self.assertTrue(form.is_valid(), "error are" + form.errors.as_text())


# class JiraApiTest(TestCase):
#
#     # setup some defaults data for this test
#     def setUp(self):
#         self.issue_dict_valid = {
#             'project': {'key': settings.TESTING_PROJECT},
#             'summary': 'This the testing summary',
#             'issuetype': {'name': 'Bug'}
#         }
#         self.issue_dict_invalid = {
#             'title': 123,
#             'type': '123',
#             'summary': None,
#             'date_registered': timezone.now(),
#             'is_solved': False
#         }
#
#     # test the JIRA api with valid data
#     def test_jira_api_with_valid_data(self):
#         created, msg = create_issue_jira(self.issue_dict_valid)
#         self.assertTrue(created, "KeyError: {0}".format(str(msg)))
#
#     # test the JIRA api with invalid data
#     def test_jira_api_with_invalid_data(self):
#         created, msg = create_issue_jira(self.issue_dict_invalid)
#         self.assertFalse(created, "KeyError: {0}".format(str(msg)))


class MockHTTPResponse(object):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def read(self):
        return self.body


class JIRAApiTest(unittest.TestCase):

    def test_issue_search(self):
        api_mock = mock.Mock()
        Issue.api = mock.Mock(return_value=api_mock)
        api_mock.get.return_value = MockHTTPResponse(200, '{"issue":[]}')
        issue = Issue.search('jql')
        api_mock.get.assert_called_with('search', {'jql': 'jql', 'fields': 'summary, status'})
        issue = Issue.search('more jql', 'summary,description')
        api_mock.get.assert_called_with('search', {'jql': 'more jql', 'fields': 'summary,description' })

    def test_issue_create(self):
        api_mock = mock.Mock()
        Issue.api = mock.Mock(return_value=api_mock)
        api_mock.send.return_value = MockHTTPResponse(201, '')
        issue = Issue.create({'project': 'ZEUS'})
        api_mock.send.assert_called_with('POST', 'issue', { 'fields': { 'project': 'ZEUS' } })