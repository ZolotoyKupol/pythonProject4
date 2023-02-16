from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Posts


class PostsList(ListView):
    model = Posts
    ordering = 'name'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class NewsDetail(DetailView):
    model = Posts
    template_name = 'flatpages/news.html'
    context_object_name = 'news'



