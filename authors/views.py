from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from authors.models import Authors
from authors.serializers import AuthorsSerializer


class AuthorsViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
