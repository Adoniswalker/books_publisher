from django.urls import path

from books.views import BooksViewSet

books_create_list = BooksViewSet.as_view({
    "post": "create",
    "get": "list",
}
)
books_detail = BooksViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', books_create_list, name='create_list_books'),
    path('<int:pk>/', books_detail, name="get_list-books")
]
