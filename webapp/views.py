# Core Django imports
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Imports from apps
from .models import Issue
from .forms import IssueForm


# Create your views here.


def home(request):
    """
    :param request:
    :return Home page:
    """

    # lists all the unsolved issues on index page
    issues = Issue.objects.filter(is_solved=False).order_by('type')

    c = {
        'issues': issues
    }

    return render(request, 'webapp/index.html', c)


# this method could be used many times, so define it as method
def create_issue_jira(issue_dict):
    # error checking to prevent the failure of API implement
    try:
        settings.AUTHED_JIRA.create_issue(fields=issue_dict)
        return {True, 'Success'}
    except Exception as error:
        return {False, error}


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

        # error checking for form
        if issue_form.is_valid():

            new_issue = issue_form.save()
            # set an dictionary for JIRA API
            issue_dict = {
                'project': {'key': settings.TESTING_PROJECT},
                'summary': new_issue.summary,
                'issuetype': {'name': new_issue.type},
            }
            # create the issue on the JIRA instance
            # TODO would need error catch as well for the issue created
            create_issue_jira(issue_dict)
            return HttpResponseRedirect(reverse('home'))
        else:
            # replace the form with form error massages
            c['issue_form'] = issue_form
    else:
        c['issue_form'] = IssueForm(request.user, instance=issue)

    return render(request, 'webapp/issue_create_edit_form.html', c)


