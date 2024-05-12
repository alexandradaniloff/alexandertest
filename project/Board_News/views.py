from django.shortcuts import render
import requests
from django.views.generic import TemplateView


from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post, Comment
from Board_News.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import PostFilter
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy



class PostList(LoginRequiredMixin, ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_created_at'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/post.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    queryset = Post.objects.all()
    paginate_by = 5

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context



class PostCreate(LoginRequiredMixin,CreateView):
    permission_required = ('post.add_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_create.html'

    # добавляем создание поста только от имени текущего пользователя
    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_author = self.request.user
        post.save()
        #send_email_task.delay(post.pk)
        return super().form_valid(form)

class PostDetail(LoginRequiredMixin, DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'flatpages/post_id.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post_id'

class PostDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('post.delete_post',)
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [ 'title', 'content', 'post_author', 'type', 'price', 'image']
    template_name = 'flatpages/post_update.html'

    # добавляем обновление поста, созданного только текущим пользователем
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        # send_email_task.delay(post.pk)
        return super().form_valid(form)

class CommentCreate(LoginRequiredMixin, CreateView):
    permission_required = ('comment.add_comment',)
    # Указываем нашу разработанную форму
    form_class = CommentForm
    # модель товаров
    model = Comment
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/comment_create.html'
    context_object_name = 'comments'

    # добавляем создание комментария только от имени текущего пользователя
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment_author = self.request.user
        comment.save()
        # send_email_task.delay(post.pk)
        return super().form_valid(form)


    # def form_valid(self, form):
    #     comment = form.save(commit=False)
    #     comment.save()
    #     #send_email_task.delay(post.pk)
    #     return super().form_valid(form)

