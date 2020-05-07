from django import forms
from .models import Issue

class IssueForm(forms.Form):
    issue_description = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'id':'id_issue_description'}))
    issue_priority = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control', 'id':'id_issue_priotity'}) ,choices=((1,'Low'), (2,'Medium'), (3,'High')))
    issue_assigned_to = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id':'id_issue_assigned_to'}))


    # def clean():
    #     pass
