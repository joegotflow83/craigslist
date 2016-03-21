from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token

from .models import Category, SubCategory, Post, UserProfile
from .forms import UserCreateForm


class Index(TemplateView):
    """First page user sees when accessing website"""
    template_name = 'main/index.html'


class Home(ListView):
    """First page when user logs in"""
    model = Category
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['token'] = Token.objects.get(user=self.request.user)
        return context


class SubCategoryThumbnailDetail(DetailView):
    model = SubCategory
    template_name = 'main/subcategory_thumbnail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newest'] = Post.objects.filter(subcategory=self.kwargs['pk'])
        return context


class SubCategoryHighestPrice(DetailView):
    model = SubCategory
    template_name = 'main/subcategory_highest_price.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['highest'] = Post.objects.filter(subcategory=self.kwargs['pk']).order_by('-price')
        return context


class SubCategoryLowestPrice(DetailView):
    model = SubCategory
    template_name = 'main/subcategory_lowest_price.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lowest'] = Post.objects.filter(subcategory=self.kwargs['pk']).order_by('price')
        return context


class SubCategoryList(SubCategoryThumbnailDetail):
    template_name = 'main/subcategory_list.html'


class SubCategoryGallery(SubCategoryThumbnailDetail):
    template_name = 'main/subcategory_gallery.html'


class PostDetail(DetailView):
    model = Post


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'description', 'price', 'image', 'city']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.subcategory = SubCategory.objects.get(pk=self.kwargs['post_id'])
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class UserCreate(CreateView):
    model = User
    form_class = UserCreateForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.user = self.request.user
        new_user.save()
        UserProfile.objects.create(user=new_user, city=form.cleaned_data['city'])
        Token.objects.create(user=new_user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class UpdateCity(UpdateView):
    model = UserProfile
    fields = ['city']

    def get_success_url(self):
        return reverse('home')

