from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class JourneyUser(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
  display_name = models.CharField(max_length=25, null=True)
  subjects = models.ManyToManyField("Subject", related_name="journeyusers", related_query_name="journeyuser")
