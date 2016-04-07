from django import forms
from webapp.models import *


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['user', 'is_solved']

    def __init__(self, user, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        issue = super(IssueForm, self).save(commit=False)
        issue.user = self.user
        if commit:
            issue.save()
        return issue