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
    """Handle GET requests to get all resources

    Returns:
      Response -- JSON serialized list of resources
    """

    caltexts = CalendarText.objects.all()

    serializer = CalTextSerializer(
      caltexts, many=True, context={'request': request})
    return Response(serializer.data)

  def create(self, request):
      """Handle POST operations

      Returns:
          response -- JSON serialized resource instance
      """

      resource = Resource()
      resource.content = request.data['content']
      resource.url = request.data['url']
      resource.category = ResourceCategory.objects.get(pk=request.data['categoryId'])
      resource.submitter = JourneyUser.objects.get(user=request.auth.user)

      try:
        resource.save()
        serializer = ResourceSerializer(resource, context={'request': request})
        return Response(serializer.data)
      
      except ValidationError as ex:
        return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class ResourceSerializer(serializers.ModelSerializer):
  """JSON Serializer for resources

  Arguments:
    serializers
  """
  class Meta:
    model = Resource
    fields = ('id', 'category', 'url', 'content', 'submitter')
    depth = 1
