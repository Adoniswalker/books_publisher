from django.urls import path

from authors.views import AuthorsViewSet

create_list_authors = AuthorsViewSet.as_view({
    "post": "create",
    "get": "list",
}
)
authors_detail = AuthorsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', create_list_authors, name='create_list_authors'),
    path('<int:pk>/', authors_detail, name="get_list")
]
