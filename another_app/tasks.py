from celery import shared_task
import requests

@shared_task(bind=True)
def test_func(self):
    #requests.post('https://back.homol.smclick.com.br/v1/api/instances/public/send_text/', json={
    #    "instance": "c8b69ccc-da38-4628-ae0b-6afc6a6dd005",
    #    "telephone": "5511964055250",
    #    "message": "teste"
    #})
    #print('deu certo!')
    return True