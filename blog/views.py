from config.settings import NOTIFICATION_THRESHOLD
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    @staticmethod
    def send_notification():
        send_mail(
            "Gratz",
            "Gratz, u got 5 views",
            "no-reply@it.ivc.vsmpo.ru",
            ["tray@it.ivc.vsmpo.ru"],
            fail_silently=False,
        )

    def get_object(self, queryset = None):
        blog_post = super().get_object(queryset)
        blog_post.views += 1
        blog_post.save()
        if blog_post.views == NOTIFICATION_THRESHOLD:
            self.send_notification()
            # пока так, вообще бы асинхронность прикрутить
        return blog_post

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]

    def get_success_url(self):
        return reverse_lazy("blog:blog_post", kwargs={"pk": self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:blog")
