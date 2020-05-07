from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Issue
from .forms import IssueForm
# Create your views here.
def show_issues(request):
    issues = Issue.objects.all().order_by('id')
    return render(request, 'issues/index.html', context={'issues':issues[::-1]})

def add_issue(request):
    valid = False
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            valid = True
            desc = form.cleaned_data['issue_description']
            priority = form.cleaned_data['issue_priority']
            assigned_to = form.cleaned_data['issue_assigned_to']
            Issue.objects.create(issue_desc=desc, issue_priority=priority, issue_assigned_to=assigned_to)
            print('Saved successfully!')
            form = IssueForm()
            # print(request.POST)
    else:
        form = IssueForm()

    return render(request, 'issues/issueForm.html', context={'form':form, 'form_valid':valid})

def delete_issue(request, issue_id):
    Issue.objects.get(id=issue_id).delete()
    print(f'Issue {issue_id} deleted!')
    return redirect('issues:list-issues')
