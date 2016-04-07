from django.shortcuts import render

# Create your views here.


def home(request):
    # The index page
    c = {}
    template = 'webapp/index.html'

    return render(request, template, c)