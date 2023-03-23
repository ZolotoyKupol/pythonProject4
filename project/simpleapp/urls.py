from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, NewsDetail, PostCreate


urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
]