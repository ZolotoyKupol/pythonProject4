from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, NewsDetail, PostCreate, PostUpdate, PostDelete, PostSearch, subscriptions


urlpatterns = [
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]