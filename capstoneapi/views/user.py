from django.contrib.auth.models import User
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from django.http import HttpResponseServerError
from capstoneapi.models import JourneyUser

class UserSerializer(serializers.ModelSerializer):
    # JSON Serializer for User
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']

class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        returns:
        Response -- JSON serialized user
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
        Response -- JSON serialized list of users
        """

        users = User.objects.all().order_by('-is_staff')

        serializer = UserSerializer(
        users, many=True, context={'request': request})
        return Response(serializer.data)
