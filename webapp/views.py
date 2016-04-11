# Core Django imports
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Imports from my apps
from .models import Issue
from .forms import IssueForm


# Create your views here.


def home(request):
    """
    :param request:
    :return Home page:
    """

    # lists all the unsolved issues
    issues = Issue.objects.filter(is_solved=False).order_by('type')

    c = {
        'issues': issues
    }

    return render(request, 'webapp/index.html', c)


@login_required()
def issue_create_edit(request):
    """
    :param request:
    :return: form page or back to home page if the form is valid.
    """

    # define some default variables
    c = {}
    issue = None

    if request.POST:
        issue_form = IssueForm(request.user, request.POST, instance=issue)

        # error checking in form
        if issue_form.is_valid():

            new_issue = issue_form.save()
            issue_dict = {
                'project': {'key': 'AJ'},
                'summary': new_issue.summary,
                'issuetype': {'name': new_issue.type},
            }
            settings.AUTHED_JIRA.create_issue(fields=issue_dict)
            return HttpResponseRedirect(reverse('home'))
        else:
            # replace the form with form error massages
            c['issue_form'] = issue_form
    else:
        c['issue_form'] = IssueForm(request.user, instance=issue)

    return render(request, 'webapp/issue_create_edit.html', c)


