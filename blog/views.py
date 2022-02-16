from django.shortcuts import render
from django.views import generic
from .models import Post

class PostView(generic.ListView):
    """Class view for the posts"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6



