from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('books/', views.book_all, name='books'),
    path('books/<int:id>/', views.book_detail, name='book_all'),
    path('add-books/', views.add_book, name='add-books'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:id>/update/', views.book_update, name='book_update'),
    path('books/<int:id>/rate/', views.book_rate, name='book_rate'),
]