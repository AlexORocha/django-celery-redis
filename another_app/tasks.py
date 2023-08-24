from celery import shared_task
import requests

@shared_task()
def test_func():
    print('deu certo!')
    return True