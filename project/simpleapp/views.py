from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django_filters.views import FilterView
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostsForm
from .filters import PostFilter
from .models import Posts



class PostsList(ListView):
    model = Posts
    ordering = 'name'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Posts
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_posts')
    raise_exception = True
    form_class = PostsForm
    model = Posts
    template_name = 'flatpages/posts_edit.html'

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.id})


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_posts')
    form_class = PostsForm
    model = Posts
    template_name = 'flatpages/posts_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_posts')
    model = Posts
    template_name = 'flatpages/posts_delete.html'

    def get_success_url(self):
        return reverse('posts_list')

class PostSearch(FilterView):
    filterset_class = PostFilter
    template_name = 'flatpages/posts_search.html'
    paginate_by = 10

    def search(request):
        filter = PostFilter(request.GET, queryset=Posts.objects.all())
        return render(request, 'search.html', {'filter': filter})







