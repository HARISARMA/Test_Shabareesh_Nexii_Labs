from django.shortcuts import render

from rest_framework import viewsets

from MyApp.models import Users

from MyApp.serializers import UserSerializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializers

