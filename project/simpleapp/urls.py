from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, NewsDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
]