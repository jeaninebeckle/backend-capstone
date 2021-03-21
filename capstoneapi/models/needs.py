from django.db import models

class Need(models.Model):
  item = models.CharField(max_length=200)
  description = models.TextField()
