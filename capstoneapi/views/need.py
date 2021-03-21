"""View module for handling requests about announcements"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Need

class NeedsViewSet(ViewSet):
  """Journey Needs"""

  def retrieve(self, request, pk=None):
    """Handle GET requests for single need

    returns:
      Response -- JSON serialized need
    """
    try:
      need = Need.objects.get(pk=pk)
      serializer = NeedSerializer(need, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    """Handle GET requests to get all needs

    Returns:
      Response -- JSON serialized list of needs
    """

    needs = Need.objects.all()

    serializer = NeedSerializer(
      needs, many=True, context={'request': request})
    return Response(serializer.data)

  def create(self, request):
      """Handle POST operations

      Returns:
          response -- JSON serialized need instance
      """

      need = Need()
      need.item = request.data["item"]
      need.description = request.data["description"]

      try:
        need.save()
        serializer = NeedSerializer(need, context={'request': request})
        return Response(serializer.data)
      
      except ValidationError as ex:
        return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None):
      """Handle DELETE requests for a single need

      Returns:
          Response -- 200, 404, or 500 status code
      """
      try:
          need = Need.objects.get(pk=pk)
          need.delete()

          return Response({}, status=status.HTTP_204_NO_CONTENT)

      except Need.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

      except Exception as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NeedSerializer(serializers.ModelSerializer):
  """JSON Serializer for needs

  Arguments:
    serializers
  """
  class Meta:
    model = Need
    fields = ('id', 'item', 'description')
