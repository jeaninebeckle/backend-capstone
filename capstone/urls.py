from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from capstoneapi.views import login_user, register_user
from rest_framework import routers
from capstoneapi.views import AnnouncementsViewSet, UserViewSet, JourneyUserViewSet, ResourcesViewSet, ResourceCategoryViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'announcements', AnnouncementsViewSet, 'announcement')
router.register(r'users', UserViewSet, 'user')
router.register(r'journeyusers', JourneyUserViewSet, 'journeyuser')
router.register(r'resources', ResourcesViewSet, 'resource')
router.register(r'categories', ResourceCategoryViewSet, 'category')
router.register(r'caltexts', CalTextViewSet, 'caltext')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
