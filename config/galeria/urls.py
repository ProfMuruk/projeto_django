from django.urls import path
from galeria.views import index, teste

urlpatterns = [
    path('', index),
    path('teste/<int:produto_id>', teste, name='teste'),
]
