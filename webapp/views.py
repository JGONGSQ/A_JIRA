from django.shortcuts import render
from jira import JIRA
from django.conf import settings


# Create your views here.


def home(request):

    options = {
        'server': 'https://jira.atlassian.com'
    }
    jira = JIRA(options)

    # print(settings.JIRA_PASSWORD, settings.JIRA_USERNAME)
    # authed_jira = JIRA(basic_auth=(str(settings.JIRA_USERNAME), str(settings.JIRA_PASSWORD)))

    # projects = authed_jira.projects()
    projects = jira.projects()
    # keys = sorted([project.key for project in projects])[2:5]
    if projects:
        for project in projects:
            print('project:', project)
    else:
        print('projects are empty')

    issue = jira.issue('JRA-1330')
    # if issues:
    #     for issue in issues:
    #         print('issue:', issue)
    # else:
    #     print('issues are empty')
    print('Issue:', issue)
    c = {
        'projects': projects,
        'issues': issue
    }

    return render(request, 'webapp/index.html', c)