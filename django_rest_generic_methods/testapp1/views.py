from django.shortcuts import render
from rest_framework import generics, status
from .serializers import BookSerializer
from .models import Book

# Create your views here.
## GET method request in DRF Generics
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

## POST method request in DRF Generics
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

## PUT method request in DRF Generics
class BookUpdateView(generics.UpdateAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

## DELETE method request in DRF Generics
class BookDestroyView(generics.DestroyAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer    


## All Generic methods(GET, POST, PUT and DELETE) into a single class

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

class BookRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    lookup_field = 'pk'   
