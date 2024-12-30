from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat_sc/<str:group_name>/", consumers.MySyncConsumer.as_asgi()),
    path("ws/chat_ac/<str:group_name>/", consumers.MyAsyncConsumer.as_asgi()),
] 