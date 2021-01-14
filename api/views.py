from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializers
from .ownpermission import ProfielPermission
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    UserのCRUD
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (ProfielPermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    ログイン済みユーザー情報のCRUD
    """
    serializer_class = UserSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """
        ログイン済みユーザー情報の取得
        """
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    """
    TaskのCRUD
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
