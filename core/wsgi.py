"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicializa la aplicación WSGI
application = get_wsgi_application()

# Aplica las migraciones automáticamente
# try:
#     # Configura Django antes de usar comandos de administración
#     django.setup()

#     # Genera migraciones
#     call_command('makemigrations', interactive=False)
#     print("Migraciones creadas correctamente.")

#     # Aplica las migraciones
#     call_command('migrate', interactive=False)
#     print("Migraciones aplicadas correctamente.")
# except Exception as e:
#     print(f"Error al aplicar migraciones: {e}")


