# Core Django imports
from django import forms
from django.utils import timezone

# Imports from apps
from .models import Issue


class IssueForm(forms.ModelForm):
    """
    Create model forms based on the Issue model
    """
    class Meta:
        model = Issue
        exclude = ['user', 'is_solved', 'date_registered']

    def __init__(self, user, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.user = user

    # register the information in the save method
    def save(self, commit=True):
        issue = super(IssueForm, self).save(commit=False)
        issue.user = self.user
        issue.date_registered = timezone.now()
        issue.is_solved = False
        if commit:
            issue.save()
        return issue
