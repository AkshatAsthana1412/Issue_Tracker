from django.db import models

# Create your models here.
class Issue(models.Model):
    issue_desc = models.CharField(max_length=150, blank=False)
    issue_priority = models.CharField(max_length=6, blank=False)
    issue_assigned_to = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.issue_desc[:11])
