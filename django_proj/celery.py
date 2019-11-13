from __future__ import absolute_import
 
import os
 
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_proj.settings') #Nota 1
 
from django.conf import settings  # Nota 2

app = Celery('proj') #Nota 1
app.config_from_object('django.conf:settings', namespace='CELERY') #Nota 2
app.autodiscover_tasks() #Nota 3
app.conf.update(
    BROKER_URL = 'redis://localhost:6379/0', #Nota 4
)