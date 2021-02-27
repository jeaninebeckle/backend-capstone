from django.db import models

class ResourceCategory(models.Model):
  label = models.CharField(max_length=50)
