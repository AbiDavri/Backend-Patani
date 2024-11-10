from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Users, TypeProject, ProjectData, UsersProyect
from .serializers import UserSerializer, TypeProjectSerializer, ProjectDataSerializer, UsersProyectSerializer

class UserListCreateView(viewsets.ModelViewSet):
    """
    View untuk menampilkan daftar pengguna dan membuat pengguna baru.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetailView(viewsets.ModelViewSet):
    """
    View untuk mengambil, memperbarui, dan menghapus pengguna berdasarkan ID.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class TypeProjectViewSet(viewsets.ModelViewSet):
    queryset = TypeProject.objects.all()
    serializer_class = TypeProjectSerializer

class UsersProyectViewSet(viewsets.ModelViewSet):
    queryset = UsersProyect.objects.all()
    serializer_class = UsersProyectSerializer

class ProjectDataViewSet(viewsets.ModelViewSet):
    queryset = ProjectData.objects.all()
    serializer_class = ProjectDataSerializer

