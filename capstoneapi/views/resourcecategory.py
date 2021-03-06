from django.contrib.auth.models import User
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from capstoneapi.models import ResourceCategory

class ResourceCategorySerializer(serializers.ModelSerializer):
    # JSON Serializer for User
    
    class Meta:
        model = ResourceCategory
        fields = ['id', 'label']

class ResourceCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing resource category instances.
    """
    serializer_class = ResourceCategorySerializer
    queryset = ResourceCategory.objects.all()

    def get_queryset(self):

        queryset = ResourceCategory.objects.all()
        return queryset
