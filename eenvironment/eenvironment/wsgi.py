"""
WSGI config for eenvironment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#Pentru rulare locala 
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eenvironment.settings')
#Pt production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eenvironment.settings_production')

application = get_wsgi_application()
 