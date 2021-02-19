from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookSerializer, AddBookToWishListSerializers
from .models import BookWishList, Book
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.


class BookView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allBook = Book.objects.all()
        serializer = BookSerializer(allBook, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)



class BookDetailsView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        getBook = Book.objects.get(pk=pk)
        serializer = BookSerializer(getBook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        getBook = Book.objects.get(pk=pk)
        serializer = BookSerializer(getBook, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    
    def delete(self, request, pk):
        getBook = Book.objects.get(pk=pk)
        getBook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddBookToWishList(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = AddBookToWishListSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)