from django.db import models


# Create your models here.
class BlogPost(models.Model):
    """

    """
    title = models.CharField(max_length=200, unique=True, verbose_name="Заголовок", help_text="Введите заголовок поста")
    content = models.TextField(verbose_name="Содержимое", help_text="Добавте содержимое поста")
    preview = models.ImageField(upload_to="blog/images/", null=True, blank=True, verbose_name="Превью", help_text="Добавьте изображение для поста")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        """Meta options for BlogPost model"""
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["created_at"]

    def __str__(self):
        return self.title
