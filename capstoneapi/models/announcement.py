from django.db import models
from django.db.models.deletion import CASCADE

class Announcement(models.Model):
  content = models.TextField()
  date = models.DateField()
  submitter = models.ForeignKey("JourneyUser", on_delete=CASCADE, related_name="announcements", related_query_name="announcement")

  class Meta:
    ordering = ["-date"]
