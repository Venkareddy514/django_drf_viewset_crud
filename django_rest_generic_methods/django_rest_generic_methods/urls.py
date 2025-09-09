"""django_rest_generic_methods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp1.views import BookListView, BookCreateView, BookUpdateView, BookDestroyView, BookListCreateAPIView ,BookRetriveUpdateDestroyAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books_get/', BookListView.as_view(), name = 'book_list'),
    path('api/books_post/', BookCreateView.as_view(), name = 'book_create'),
    path('api/books_update/<int:pk>/', BookUpdateView.as_view(), name = 'book_update'),
    path('api/books_destroy/<int:pk>/', BookDestroyView.as_view(), name = 'book_delete'),
    path('book/', BookListCreateAPIView.as_view(), name='book-list-create-view'),
    path('book/<int:pk>/', BookRetriveUpdateDestroyAPIView.as_view(), name='book-retrive-update-destroy-view'),



]
