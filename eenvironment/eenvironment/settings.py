import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key din variabilă de mediu
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-fallback-key')

# Debug în funcție de mediu
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Render domain exact
ALLOWED_HOSTS = ['eenvironment.onrender.com']

# Aplicații Django + 3rd-party
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'eenvironmentblog',
    'ckeditor',
    'ckeditor_uploader',
    'allauth',
    'allauth.account',
    'django_extensions',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # important
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'eenvironment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eenvironment.wsgi.application'

# SQLite – atenție: datele NU sunt persistente pe Render după deploy/restart
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validați parolele (poți comenta în dev/test)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ro-ro'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_TZ = True

# Fișiere statice & WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media – pentru imagini încărcate
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'

# Redirecționare după login
LOGIN_REDIRECT_URL = '/'

# Django Extensions – pentru grafuri de modele etc.
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 