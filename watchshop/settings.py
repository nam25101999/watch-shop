ALLOWED_HOSTS = ['nhokvodanh2510.pythonanywhere.com', '127.0.0.1', 'localhost']
from django.utils.translation import gettext_lazy as _

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from decouple import config

SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# settings.py

# Ngôn ngữ mặc định
LANGUAGE_CODE = 'vi'

# Bật dịch ngôn ngữ
USE_I18N = True

# Danh sách ngôn ngữ hỗ trợ
LANGUAGES = [
    ('vi', _('Vietnamese')),
    ('en', _('English')),
    ('fr', _('French')),
    ('de', _('German')),
    ('es', _('Spanish')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('zh-hans', _('Chinese (Simplified)')),
    ('ru', _('Russian')),
    ('it', _('Italian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]




# Application definition



INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'core',
    'products',
    'cart',
    'orders',
    'wishlist',
    'reviews',
    'notifications',
    'messenger',
    'search',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'watchshop.urls'


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
                'django.template.context_processors.i18n',
                'products.context_processors.menu_processor',
                'messenger.context_processors.chat_data',
            ],
        },
    },
]


WSGI_APPLICATION = 'watchshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
AUTH_USER_MODEL = 'users.CustomUser'

from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#    'default': {
  #      'ENGINE': 'django.db.backends.postgresql',
 #       'NAME': config('DB_NAME'),
 #       'USER': config('DB_USER'),
 #       'PASSWORD': config('DB_PASSWORD'),
 #       'HOST': config('DB_HOST'),
 #       'PORT': config('DB_PORT'),
 #   }
#}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
