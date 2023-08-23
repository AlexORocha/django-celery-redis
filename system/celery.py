# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")
app = Celery("system")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.enable_utc = False
app.conf.update(timezone="America/Sao_Paulo")
app.conf.beat_schedule = {
    
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')