from django.db import models

class Subject(models.Model):
  label = models.CharField(max_length=150)

  class Meta:
    ordering = ["label"]
