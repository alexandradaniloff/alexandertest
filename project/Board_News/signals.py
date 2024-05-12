from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


from .models import Comment
from django.contrib.auth.models import User

@receiver(post_save, sender=Comment)
def create_comment(sender, instance, created, **kwargs):
    if created:

        html_content = render_to_string(
            'flatpages/comment_create_email.html',
            {
                'text': f'''Пользователь {instance.comment_author.username}, откликнулся на ваше объявление: '{instance.post.title}'. ''' ,
                'link': f'{settings.SITE_URL}{instance.post.id}',
            }
        )
        msg = EmailMultiAlternatives(

            subject = 'Отклик на объявление',
            body = '',
            from_email = 'alexandradaniloff@mail.ru',
            to = ['alexandradaniloff@gmail.com'],
            )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


