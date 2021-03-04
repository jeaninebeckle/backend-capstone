from rest_framework import viewsets, serializers
from rest_framework.response import Response
from django.http import HttpResponseServerError
from capstoneapi.models import JourneyUser

class JourneyUserSerializer(serializers.ModelSerializer):
    # JSON Serializer for User
    
    class Meta:
        model = JourneyUser
        fields = ['id', 'display_name']

class JourneyUserViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        returns:
        Response -- JSON serialized user
        """
        try:
            user = JourneyUser.objects.get(pk=pk)
            serializer = JourneyUserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
        Response -- JSON serialized list of users
        """

        users = JourneyUser.objects.all()

        serializer = JourneyUserSerializer(
        users, many=True, context={'request': request})
        return Response(serializer.data)
