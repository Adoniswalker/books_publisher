from django.urls import path

from authors.views import AuthorsViewSet
create_list_authors = AuthorsViewSet.as_view({
    "post": "create",
    "get": "list",
    }
)

urlpatterns = [
    path('', create_list_authors, name='create_list_authors')
]
