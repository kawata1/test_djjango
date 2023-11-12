from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'category': ['icontains'],
           'created_at': ['gt']
       }