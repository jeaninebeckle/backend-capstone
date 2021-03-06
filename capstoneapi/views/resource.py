"""View module for handling requests about resources"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Resource, JourneyUser, ResourceCategory

class ResourcesViewSet(ViewSet):
  """Journey Resources"""

  def retrieve(self, request, pk=None):
    """Handle GET requests for single resource

    returns:
      Response -- JSON serialized category
    """
    try:
      resource = Resource.objects.get(pk=pk)
      serializer = ResourceSerializer(resource, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    """Handle GET requests to get all resources

    Returns:
      Response -- JSON serialized list of resources
    """

    resources = Resource.objects.all()

    serializer = ResourceSerializer(
      resources, many=True, context={'request': request})
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
