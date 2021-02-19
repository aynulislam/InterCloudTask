from rest_framework import serializers
from .models import Book, BookWishList

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookToWishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookWishList
        fields = '__all__'

