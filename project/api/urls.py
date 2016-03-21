from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^categories/$', views.CategoryListAPIView.as_view(), name='category_list_api'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryRetrieveAPIView.as_view(), name='category_retrieve_api'),
    url(r'^subcategories/$', views.SubCategoryListAPIView.as_view(), name='subcategory_list_api'),
    url(r'^subcategories/(?P<pk>\d+)/$', views.SubCategoryRetrieveAPIView.as_view(), name='subcategories_retrieve_api'),
    url(r'^category/posts/$', views.CategoryPostsListAPIView.as_view(), name='category_posts_list_api'),
    url(r'^subcategory/posts/$', views.SubCategoryPostsListAPIView.as_view(), name='subcategory_post_list_api'),
    url(r'^category/(?P<pk>\d+)/posts/$', views.CategoryPostsRetrieveAPIView.as_view(), name='category_posts_retrieve_api'),
    url(r'^subcategory/(?P<pk>\d+)/posts/$', views.SubCategoryPostsRetrieveAPIView.as_view(), name='subcategory_posts_retrieve_api'),
    url(r'^posts/$', views.PostListCreateAPIView.as_view(), name='post_list_create_api'),
    url(r'post/(?P<pk>\d+)/$', views.PostRetrieveUpdateAPIView.as_view(), name='post_retrieve_update_api'),
]
