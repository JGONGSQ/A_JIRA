from django.shortcuts import render
from jira import JIRA
from django.conf import settings
from webapp.models import *
from webapp.forms import *
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):

    # options = {
    #     'server': 'https://jira.atlassian.com'
    # }
    # jira = JIRA(options)

    # print(settings.JIRA_PASSWORD, settings.JIRA_USERNAME)
    # authed_jira = JIRA(basic_auth=(str(settings.JIRA_USERNAME), str(settings.JIRA_PASSWORD)))

    # projects = authed_jira.projects()
    # projects = jira.projects()
    # keys = sorted([project.key for project in projects])[2:5]
    # if projects:
    #     for project in projects:
    #         print('project:', project)
    # else:
    #     print('projects are empty')
    #
    # issue = jira.issue('JRA-1330')
    # if issues:
    #     for issue in issues:
    #         print('issue:', issue)
    # else:
    #     print('issues are empty')
    # print('Issue:', issue)
    issues = Issue.objects.filter(is_solved=False).order_by('type')

    c = {
        # 'projects': projects,
        'issues': issues
    }

    return render(request, 'webapp/index.html', c)


def issue_create_edit(request):
    c = {}
    user = request.user

    issue = None

    if request.POST:
        issue_form = IssueForm(request.POST, instance=issue)
        if issue_form.is_valid():
            new_issue = issue_form.save()
            return HttpResponseRedirect('home')
        else:
            c['issue_form'] = issue_form
    else:
        c['issue_form'] = IssueForm(user, instance=issue)

    return render(request, 'webapp/issue_create_edit.html', c)


