import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('my_site')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
