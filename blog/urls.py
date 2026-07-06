from django.urls import path

from blog.apps import BlogConfig

from . import views

app_name = BlogConfig.name

urlpatterns = [
    path("", views.BlogPostListView.as_view(), name="blog"),
    path("post/<int:pk>", views.BlogPostDetailView.as_view(), name="blog_post"),
    path("post/new", views.BlogPostCreateView.as_view(), name="blog_post_new"),
    path("post/<int:pk>/edit", views.BlogPostUpdateView.as_view(), name="blog_post_edit"),
    path("post/<int:pk>/delete", views.BlogPostDeleteView.as_view(), name="blog_post_delete"),
]
