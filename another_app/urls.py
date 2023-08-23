from django.urls import path, include
from another_app.views import test

urlpatterns = [
    path('', test, name='test'),
]
