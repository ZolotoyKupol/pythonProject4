from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Posts

@receiver(post_save, sender=Posts)
def post_created(instance, created,  **kwargs):
    # print('Появилась новость', instance)
    if not created:
        return

    emails = User.objects.filter(
        subscriber__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая новость в категории {instance.category}'

    text_content = (
        f'Товар: {instance.name}\n'
        f'Ссылка на новость: http://127.0.0.1{instance.get_absolute_url()}'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
