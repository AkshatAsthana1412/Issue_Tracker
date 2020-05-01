from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_issues(request):
    return HttpResponse('The list of issues goes here')


def add_issue(request):
    return HttpResponse('the form to add a new issue here')
