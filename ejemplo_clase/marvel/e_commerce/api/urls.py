from django.urls import path
from e_commerce.api.hello_world_api import *
from e_commerce.api.marvel_api_views import *
from . import views

urlpatterns = [
    path('hello-world/',hello_world),
    path('request-data/',return_request_data),
    path('get_comics/',get_comics),
    path('purchased_item/',purchased_item),
    
    path('hola-get/', views.obtener_get),
    path('hola-post/', views.obtener_post),
    path('hola-get-post/', views.obtner_get_post),
]
 