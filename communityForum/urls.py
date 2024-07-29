from django.urls import path
from .views import CategoryListCreateView, ThreadListCreateView, ThreadDetailView, PostListCreateView, PostDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(),
         name='category_list_create'),
    path('threads/', ThreadListCreateView.as_view(), name='thread_list_create'),
    path('threads/<slug:thread_slug>/',
         ThreadDetailView.as_view(), name='thread_detail'),
    path('threads/<slug:thread_slug>/posts/',
         PostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]