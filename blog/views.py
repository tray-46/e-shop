from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog")


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:blog")
