from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListCreateView, UserDetailView, ProjectDataViewSet, TypeProjectViewSet, UsersProyectViewSet

router = DefaultRouter()
router.register(r'users', UserListCreateView, basename='user')
router.register(r'users/<int:pk>', UserDetailView, basename='user-detail')

router.register(r'users_proyect', UsersProyectViewSet, basename='users_proyect')
router.register(r'projects', ProjectDataViewSet, basename='project')
router.register(r'types', TypeProjectViewSet, basename='type')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]