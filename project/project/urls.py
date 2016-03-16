"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.views.static import serve
from django.contrib.auth.decorators import login_required

from main import views
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^signup/$', views.UserCreate.as_view(), name='signup'),
    url(r'^accounts/login/$', auth_view.login, name='login'),
    url(r'^accounts/logout/$', auth_view.logout_then_login, name='logout'),
    url(r'^update/city/(?P<pk>\d+)/$', views.UpdateCity.as_view(), name='update_city'),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^subcategory/thumbnail/(?P<pk>\d+)/$', views.SubCategoryThumbnailDetail.as_view(), name='subcategory_thumbnail'),
    url(r'^subcategory/list/(?P<pk>\d+)/$', views.SubCategoryList.as_view(), name='subcategory_list'),
    url(r'^subcategory/gallery/(?P<pk>\d+)/$', views.SubCategoryGallery.as_view(), name='subcategory_gallery'),
    url(r'^subcategory/posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^subcategory/create/post/(?P<post_id>\d+)/$', login_required(views.CreatePost.as_view()), name='create_post'),
    url(r'^subcategory/highest/price/(?P<pk>\d+)/$', views.SubCategoryHighestPrice.as_view(), name='subcategory_highest'),
    url(r'^subcategory/lowest/price/(?P<pk>\d+)/$', views.SubCategoryLowestPrice.as_view(), name='subcategory_lowest'),
]
