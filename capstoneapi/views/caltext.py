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

  def retrieve(self, request, pk=None):
    """Handle GET requests for single text

    returns:
      Response -- JSON serialized text
    """
    try:
      text = CalendarText.objects.get(pk=pk)
      serializer = CalTextSerializer(text, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex) 

  def update(self, request, pk=None):
      """Handle PUT requests for cal text

      Returns:
          Response -- Empty body with 204 status code
      """
      calText = CalendarText.objects.get(pk=pk)
      calText.content = request.data["content"]
  
      calText.save()

      return Response({}, status=status.HTTP_204_NO_CONTENT)

  
class CalTextSerializer(serializers.ModelSerializer):
  """JSON Serializer for calendar text

  Arguments:
    serializers
  """
  class Meta:
    model = CalendarText
    fields = ('id', 'content', 'name')
