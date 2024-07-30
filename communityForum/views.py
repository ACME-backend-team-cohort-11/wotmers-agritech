from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Category, Thread, Post
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class to set standard pagination settings.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of categories or create a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class ThreadListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of threads or create a new thread.
    """
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        """
        Optionally restricts the returned threads to a given category,
        by filtering against a `category_id` query parameter in the URL.
        """
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            return Thread.objects.filter(category_id=category_id, is_published=True)
        return Thread.objects.filter(is_published=True)

    def perform_create(self, serializer):
        """
        Sets the author of the thread to the current user.
        """
        serializer.save(author=self.request.user)


class ThreadDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a thread instance.
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Ensures that only the author or an admin can update the thread.
        """
        instance = self.get_object()
        if instance.author != self.request.user and not self.request.user.is_staff:
            raise permissions.PermissionDenied(
                "You do not have permission to edit this thread.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures that only the author or an admin can delete the thread.
        """
        if instance.author != self.request.user and not self.request.user.is_staff:
            raise permissions.PermissionDenied(
                "You do not have permission to delete this thread.")
        instance.delete()


class PostListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of posts or create a new post.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned posts to a given thread,
        by filtering against a `thread_slug` parameter in the URL.
        """
        thread_slug = self.kwargs.get('thread_slug')
        return Post.objects.filter(thread__slug=thread_slug, is_approved=True)

    def perform_create(self, serializer):
        """
        Sets the author of the post to the current user and associates it with the specified thread and parent post.
        """
        thread_slug = self.kwargs.get('thread_slug')
        thread = get_object_or_404(Thread, slug=thread_slug)
        parent_post_id = self.request.data.get('parent_post')
        parent_post = get_object_or_404(
            Post, id=parent_post_id) if parent_post_id else None
        serializer.save(author=self.request.user,
                        thread=thread, parent_post=parent_post)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a post instance.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Ensures that only the author or an admin can update the post.
        """
        instance = self.get_object()
        if instance.author != self.request.user and not self.request.user.is_staff:
            raise permissions.PermissionDenied(
                "You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures that only the author or an admin can delete the post.
        """
        if instance.author != self.request.user and not self.request.user.is_staff:
            raise permissions.PermissionDenied(
                "You do not have permission to delete this post.")
        instance.delete()