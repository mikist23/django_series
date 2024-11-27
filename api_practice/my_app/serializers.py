from rest_framework import serializers
from .models import Book, Post

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','title','content','author','created_at']
