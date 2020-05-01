from django.urls import path
from . import views
app_name = 'issues'

urlpatterns = [
    path('', views.show_issues, name='list-issues'),
    path('new-issue/', views.add_issue, name='new-issue'),
]
