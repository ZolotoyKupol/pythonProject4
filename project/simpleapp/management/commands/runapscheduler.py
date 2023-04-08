from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import timezone
from simpleapp.models import Subscriber, Category, Posts
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.schedulers import BackgroundScheduler
from django.core.management.base import BaseCommand
from simpleapp.tasks import send_articles_to_subscribers


def send_articles_to_subscribers():
    subscribers = Subscriber.objects.all()
    new_posts = Posts.objects.filter(publish_date__gte=timezone.now() - timezone.timedelta(days=7))

    for subscriber in subscribers:
        categories = Category.objects.filter(name__in=subscriber.categories.all())
        subscriber_posts = new_posts.filter(category__in=categories)

        if subscriber_posts.exists():
            subject = 'Новые статьи в категориях: {}'.format(', '.join([c.name for c in categories]))
            body = render_to_string('email/new_posts.html', {'subscriber': subscriber, 'posts': subscriber_posts})
            email = EmailMessage(subject, body, to=[subscriber.email])
            email.send()


class Command(BaseCommand):
    help = 'Runs APScheduler'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler(timezone='UTC')
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        # Запускать каждую пятницу в 18:00
        scheduler.add_job(send_articles_to_subscribers, 'cron', day_of_week='fri', hour=18)

        scheduler.start()
        print('Scheduler started...')