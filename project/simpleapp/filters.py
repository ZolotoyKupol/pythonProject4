from django_filters import FilterSet
from .models import Posts

class PostFilter(FilterSet):
    class Meta:
        model = Posts
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
            'date': ['gt'],
            'description': ['icontains']
        }