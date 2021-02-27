from django.db import models
from django.db.models.deletion import CASCADE

class Resource(models.Model):
  category = models.ForeignKey("ResourceCategory", on_delete=CASCADE, related_name="resources", related_query_name="resource")
  content = models.CharField(max_length=100)
  url = models.CharField(max_length=500)
  submitter = models.ForeignKey("JourneyUser", on_delete=CASCADE, related_name="resources", related_query_name="resource")
