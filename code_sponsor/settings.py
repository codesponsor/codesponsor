import socket
import environ


root = environ.Path(__file__) - 2         # Set the base directory to two levels
env = environ.Env(DEBUG=(bool, False), )  # set default values and casting

try:
    env.read_env(str(root.path('app/.env')))  # reading .env file
except:
    pass

DEBUG = env.bool('DEBUG', default=True)
ENV = env('ENV', default='local')
HOSTNAME = env('HOSTNAME', default=socket.gethostname())

BASE_URL = env('BASE_URL', default='http://localhost:8000/')
SECRET_KEY = env('SECRET_KEY', default='YOUR-SupEr-SecRet-KeY')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = root()


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
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

ROOT_URLCONF = env('ROOT_URLCONF', default='code_sponsor.urls')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root.path('templates')]
        ,
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

WSGI_APPLICATION = env('WSGI_APPLICATION', default='code_sponsor.wsgi.application')

# Database
DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')
USE_I18N = env.bool('USE_I18N', default=True)
USE_L10N = env.bool('USE_L10N', default=True)
USE_TZ = env.bool('USE_TZ', default=True)
TIME_ZONE = env('TIME_ZONE', default='UTC')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = env.tuple('STATICFILES_DIRS', default=('assets/', ))
STATIC_ROOT = root('static')
STATIC_URL = env('STATIC_URL', default='/static/')