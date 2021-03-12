"""View module for handling requests about resources"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Subject

class SubjectViewSet(ViewSet):
  """Journey Subjects"""

  def retrieve(self, request, pk=None):
    """Handle GET requests for single subject

    returns:
      Response -- JSON serialized subject
    """
    try:
      subject = Subject.objects.get(pk=pk)
      serializer = SubjectSerializer(subject, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    """Handle GET requests to get all subjects

    Returns:
      Response -- JSON serialized list of subjects
    """

    subjects = Subject.objects.all().order_by('label')

    serializer = SubjectSerializer(
      subjects, many=True, context={'request': request})
    return Response(serializer.data)


class SubjectSerializer(serializers.ModelSerializer):
  """JSON Serializer for subjects
  Arguments:
    serializers
  """
  class Meta:
    model = Subject
    fields = ('id', 'label')
