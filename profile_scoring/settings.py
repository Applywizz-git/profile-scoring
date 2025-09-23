from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# Load .env file (optional)
# =====================
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

# =====================
# Security settings
# =====================
SECRET_KEY = env('DJANGO_SECRET_KEY', default=os.getenv('DJANGO_SECRET_KEY'))  # Make sure to set this in Render
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['your-app-name.onrender.com', 'localhost', '127.0.0.1']  # Add Render URL

# =====================
# Application definition
# =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scoring',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'profile_scoring.urls'

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

WSGI_APPLICATION = 'profile_scoring.wsgi.application'

# =====================
# Database settings for Render
# =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='your-db-name'),  # Set in Render environment variables
        'USER': env('DB_USER', default='your-db-user'),
        'PASSWORD': env('DB_PASSWORD', default='your-db-password'),
        'HOST': 'localhost',  # PostgreSQL database URL
        'PORT': '5432',  # Default PostgreSQL port
    }
}

# =====================
# Password validation
# =====================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# =====================
# Email settings for Outlook
# =====================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'  # SMTP server for Outlook
EMAIL_PORT = 587  # Standard port for TLS
EMAIL_USE_TLS = True  # Use TLS encryption
EMAIL_HOST_USER = env('OUTLOOK_SENDER_EMAIL')  # Your Outlook email (set in environment variables)
EMAIL_HOST_PASSWORD = env('OUTLOOK_CLIENT_SECRET')  # Your application password or client secret (OAuth2)
DEFAULT_FROM_EMAIL = env('OUTLOOK_SENDER_EMAIL')  # Same email as your sender email
EMAIL_TIMEOUT = 30  # Timeout for sending emails

# =====================
# Static files settings for Render
# =====================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Render will serve static files from this directory

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# =====================
# Default primary key field type
# =====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =====================
# Security settings for production
# =====================
SECURE_SSL_REDIRECT = True  # Ensure all traffic is redirected to HTTPS
CSRF_COOKIE_SECURE = True  # Use secure cookies
SESSION_COOKIE_SECURE = True  # Use secure cookies
