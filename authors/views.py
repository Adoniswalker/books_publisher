
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from authors.models import Authors
from authors.serializers import AuthorsSerializer
from books.paginations import StandardResultsSetPagination


class AuthorsViewSet(ModelViewSet):
    queryset = Authors.objects.get_queryset().order_by('id')
    serializer_class = AuthorsSerializer
    pagination_class = StandardResultsSetPagination
