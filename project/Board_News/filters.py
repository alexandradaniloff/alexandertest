from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms

class PostFilter(FilterSet):
    date_created = DateFilter(field_name='post_created_at', widget=forms.DateInput(attrs={'type': 'date'}),
                             lookup_expr='date__gte')
    class Meta:
        model = Post
        fields = {
           # поиск по названию
           'title': ['istartswith'],
           'type': ['iexact'],

        }