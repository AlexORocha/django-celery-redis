# django-celery-redis

Repositório utilizado para aprender a trabalhar com o Celery e o Redis dentro de um projeto Django.

# Iniciar o Celery Beat

celery -A system beat -l INFO

# Iniciar o Celery Worker

celery -A system.celery worker -l info

# Iniciar o Redis

No terminal WSL (Ubuntu): redis-server
