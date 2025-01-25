"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicializa la aplicación WSGI
application = get_wsgi_application()

# Aplica las migraciones automáticamente
try:
    django.setup()  # Configura Django antes de usar comandos de administración
    call_command('migrate', interactive=False)
    print("Migraciones aplicadas correctamente.")
except Exception as e:
    print(f"Error al aplicar migraciones: {e}")


# Creando superusuario
User = get_user_model()

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superusuario creado con éxito.")
except Exception as e:
    print(f"Error al crear el superusuario: {e}")
