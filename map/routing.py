from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('chat/ws/<str:room_name>', consumers.ChatConsumer.as_asgi()),
]