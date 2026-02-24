import os
from pathlib import Path
import dj_database_url

# ------------------------------------------------------------
# BASE DIRECTORY
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-key"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "mon-back-w4sx.onrender.com",
    "localhost",
    "127.0.0.1",
]

# ------------------------------------------------------------
# INSTALLED APPS
# ------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'library',
]

# ------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 static Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------
# URLS & WSGI
# ------------------------------------------------------------
ROOT_URLCONF = 'school_doc_backend.urls'
WSGI_APPLICATION = 'school_doc_backend.wsgi.application'

# ------------------------------------------------------------
# TEMPLATES
# ------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# ------------------------------------------------------------
# DATABASE (Render auto)
# ------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

# ------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------
# STATIC FILES
# ------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ------------------------------------------------------------
# REST FRAMEWORK
# ------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# ------------------------------------------------------------
# CORS
# ------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://mon-back-w4sx.onrender.com",
]

# ------------------------------------------------------------
# DEFAULT PK
# ------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'