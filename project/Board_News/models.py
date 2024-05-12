from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
#from users.models import ReplyFilter

class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Post(models.Model):
    TYPES = [
        ('TANK', 'Танк'),
        ('HILL', 'Хилл'),
        ('DD', 'ДД'),
        ('MER', 'Торговец'),
        ('GILD', 'Гилдмастер'),
        ('KV', 'Квестгивер'),
        ('BS', 'Кузнец'),
        ('TAN', 'Кожевник'),
        ('ZE', 'Зельевар'),
        ('MI', 'Мастер заклинаний'),
    ]
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    post_updated_ad = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    type = models.CharField(max_length=4, choices=TYPES, blank=False, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True)

    def __str__(self):
        return f'{self.post_author} : {self.content}'

    # def preview(self):
    #     preview = f'{self.content[:50]}'
    #     return preview
    #
    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['post_created_at']

    def get_absolute_url(self):
        return reverse('post')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='PostComment')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'author', verbose_name="Автор")
    content = models.TextField(verbose_name="Описание")
    comment_created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name="Статус")


    def __str__(self):
        return f'{self.comment_author} : {self.content}'

    def priview(self):
        preview = f' {self.text[:124]}'
        return preview

    def get_absolute_url(self):
        return reverse('post')


    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['id']

