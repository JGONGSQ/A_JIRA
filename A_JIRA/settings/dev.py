from .base import *


SECRET_KEY = '+92261zuxi5@wp=x%!k(+0vs46jo%q=)u45&3bf852=qz5pmbl'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'a_jira',
        'USER': 'root'
    }
}

TESTING_PROJECT = 'AJ'

from jira import JIRA
AUTHED_JIRA = JIRA(server='https://jamesjira.atlassian.net', basic_auth=('admin', 'admin'))
