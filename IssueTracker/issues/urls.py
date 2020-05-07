from django.urls import path
from . import views
app_name = 'issues'

urlpatterns = [
    path('', views.show_issues, name='list-issues'),
    path('add-issue/', views.add_issue, name='new-issue'),
    path('delete/<int:issue_id>', views.delete_issue, name='delete-issue'),
]
