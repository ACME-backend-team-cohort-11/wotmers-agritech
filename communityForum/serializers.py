from rest_framework import serializers
from .models import Category, Thread, Post


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug',
                  'description', 'created_at', 'updated_at']


class ThreadSerializer(serializers.ModelSerializer):
    """
    Serializer for the Thread model.
    """
    class Meta:
        model = Thread
        fields = ['id', 'title', 'slug', 'content', 'category',
                  'author', 'is_published', 'tags', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    class Meta:
        model = Post
        fields = ['id', 'content', 'thread', 'author',
                  'parent_post', 'is_approved', 'created_at', 'updated_at']