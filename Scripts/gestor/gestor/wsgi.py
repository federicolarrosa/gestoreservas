import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
"""
WSGI config for gestor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

os.environ["DJANGO_SETTINGS_MODULE"] = "{{ gestor }}.settings"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
