from datetime import datetime

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
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


class PostCreate(CreateView):
    form_class = PostsForm
    model = Posts
    template_name = 'flatpages/posts_edit.html'

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.id})








