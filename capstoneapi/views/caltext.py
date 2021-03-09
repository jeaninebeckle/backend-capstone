"""View module for handling requests about resources"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import CalendarText

class CalTextViewSet(ViewSet):
  """Journey Calendar text"""

  def list(self, request):
    """Handle GET requests to get calendar text

    Returns:
      Response -- JSON serialized calendar text
    """

    caltexts = CalendarText.objects.all()

    serializer = CalTextSerializer(
      caltexts, many=True, context={'request': request})
    return Response(serializer.data)

  
class CalTextSerializer(serializers.ModelSerializer):
  """JSON Serializer for calendar text

  Arguments:
    serializers
  """
  class Meta:
    model = CalendarText
    fields = ('id', 'content', 'name')
