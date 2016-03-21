from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

from .serializers import CategorySerializer, SubCategorySerializer, PostSerializer
from main.models import Category, SubCategory, Post


class CategoryListAPIView(generics.ListAPIView):
    """Display list of categorys endpoint"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    """Display a single category endpoint"""
    serializer_class = CategorySerializer

    def get_object(self):
        return Category.objects.get(id=self.kwargs['pk'])


class SubCategoryListAPIView(generics.ListAPIView):
    """Display list of subcategories endpoint"""
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    """Dipslay a single subcategory endpoint"""
    serializer_class = SubCategorySerializer

    def get_object(self):
        return SubCategory.objects.get(id=self.kwargs['pk'])


class CategoryPostsListAPIView(generics.ListAPIView):
    """Display posts from all categories endpoint"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class SubCategoryPostsListAPIView(generics.ListAPIView):
    """Display posts from all subcategories endpoint"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoryPostsRetrieveAPIView(generics.RetrieveAPIView):
    """Display posts from a particular category"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs['pk'])


class SubCategoryPostsRetrieveAPIView(generics.RetrieveAPIView):
    """Display posts from a particular subcategory"""
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(subcategory=self.kwargs['pk'])


class PostListCreateAPIView(generics.ListCreateAPIView):
    """Display Create a post endpoint"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Display a single post and update the post"""
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Post.objects.filter(Q(id=self.kwargs['pk']), Q(user=self.request.user))
