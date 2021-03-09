from django.db import models

class CalendarText(models.Model):
  content = models.TextField()
  name = models.CharField(max_length=100)
