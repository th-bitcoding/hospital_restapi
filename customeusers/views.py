from django.shortcuts import render
from rest_framework import viewsets
from customeusers.serializers import UserSerializers
from customeusers.models import CustomeUser


class UserModelView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = CustomeUser.objects.all()
