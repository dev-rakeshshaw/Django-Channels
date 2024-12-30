"""
ASGI config for main_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# import app.routing
# import chat_app.routing
from app.routing import websocket_urlpatterns as app_websocket_urlpatterns
from chat_app.routing import websocket_urlpatterns as chat_app_websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_project.settings')

websocket_urlpatterns = app_websocket_urlpatterns + chat_app_websocket_urlpatterns

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
})
