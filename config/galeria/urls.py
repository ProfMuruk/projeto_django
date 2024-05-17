from django.urls import path
from galeria.views import index, teste

urlpatterns = [
    path('', index),
    path('teste/', teste, name='teste'),
]
