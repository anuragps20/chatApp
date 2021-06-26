"""
ASGI config for chatRoom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatRoom.settings')

# application = get_asgi_application()

import os
import django
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatRoom.settings")
django.setup()
from chatApp.routing import websocket_urlpatterns

from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),

})