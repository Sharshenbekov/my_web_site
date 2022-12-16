from django.urls import path
from .views import index, create, add_fruit


urlpatterns = [
    path('', index, name='name'),
    path('create/', create, name='create'),
    path('add_fruit/', add_fruit, name='add_fruit'),
]
