from rest_framework import generics, permissions
from .models import Category, Thread, Post
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ThreadListCreateView(generics.ListCreateAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            return Thread.objects.filter(category_id=category_id, is_published=True)
        return Thread.objects.filter(is_published=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ThreadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        thread_slug = self.kwargs.get('thread_slug')
        return Post.objects.filter(thread__slug=thread_slug, is_approved=True)

    def perform_create(self, serializer):
        thread_slug = self.kwargs.get('thread_slug')
        thread = Thread.objects.get(slug=thread_slug)
        parent_post_id = self.request.data.get('parent_post')
        parent_post = Post.objects.get(
            id=parent_post_id) if parent_post_id else None
        serializer.save(author=self.request.user,
                        thread=thread, parent_post=parent_post)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]