from django_filters import FilterSet, DateFilter
from .models import Posts

class PostFilter(FilterSet):
    date = DateFilter(field_name='date', lookup_expr='gte')
    class Meta:
        model = Posts
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
            'description': ['icontains']
        }