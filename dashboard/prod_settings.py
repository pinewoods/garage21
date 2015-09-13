WSGI_APPLICATION = 'dashboard.wsgi.application'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DEBUG = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT =path.join(BASE_DIR,'static')
STATIC_URL =path.join(BASE_DIR,'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )