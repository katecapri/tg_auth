from django.urls import path
from src.link.consumers import WSConsumer

ws_urlpatterns = [
    path('ws/auth/<str:token>/', WSConsumer.as_asgi())
]