from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()