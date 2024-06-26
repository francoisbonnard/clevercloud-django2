"""
WSGI config for photoshare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photoshare.settings')

application = get_wsgi_application()


from django.contrib.auth.models import User
from decouple import config

def create_super_user():
    if not User.objects.filter(username='fransua').exists():
        User.objects.create_superuser('fransua', 'geosesame@gmail.com', config('PASSWORD_SUPERUSER'))

# create_super_user()

