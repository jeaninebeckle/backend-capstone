from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from django.http import HttpResponseServerError
from capstoneapi.models import JourneyUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # JSON Serializer for User  
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']

class JourneyUserSerializer(serializers.ModelSerializer):
    # JSON Serializer for User

    user=UserSerializer(many=False)
    class Meta:
        model = JourneyUser
        fields = ['id', 'display_name', 'user', 'subjects']

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


    def update(self, request, pk=None):
        """Handle PUT requests for changing the tutoring subjects for a Journey user

        Returns:
            Response -- Empty body with 204 status code
        """
        user = JourneyUser.objects.get(pk=pk)
        user.subjects.set(request.data["subjects"])
    
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
