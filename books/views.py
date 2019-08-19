from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from books.models import Books
from books.paginations import StandardResultsSetPagination
from books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.get_queryset().order_by('id')
    serializer_class = BooksSerializer
    pagination_class = StandardResultsSetPagination
