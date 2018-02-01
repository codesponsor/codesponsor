import socket

import environ

root = environ.Path(__file__) - 2  # Set the base directory to two levels
env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
try:
    env.read_env()
except IOError:
    pass

DEBUG = env.bool('DEBUG', default=True)
ENV = env('ENV', default='local')
HOSTNAME = env('HOSTNAME', default=socket.gethostname())
BASE_URL = env('BASE_URL', default='http://localhost:8000/')
SECRET_KEY = env('SECRET_KEY', default='YOUR-SupEr-SecRet-KeY')
BASE_DIR = root()
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    'app.templatetags.app_extras',
    'home',
    'track',
    'storages',
    'anymail',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = env('ROOT_URLCONF', default='code_sponsor.urls')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root.path('templates'),
            root.path('templates/allauth')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',

                # google analytics
                'app.context_processors.ga_tracking_id',
                'app.context_processors.use_ga',
            ],
        },
    },
]

WSGI_APPLICATION = env(
    'WSGI_APPLICATION', default='code_sponsor.wsgi.application')

# Database
DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')
USE_I18N = env.bool('USE_I18N', default=True)
USE_L10N = env.bool('USE_L10N', default=True)
USE_TZ = env.bool('USE_TZ', default=True)
TIME_ZONE = env('TIME_ZONE', default='UTC')

# Static Assets
STATIC_ROOT = str(root.path('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(root.path('static')),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROLLBAR = {
    'access_token': env(
        'ROLLBAR_ACCESS_TOKEN', default='ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': BASE_DIR,
    'patch_debugview': False,
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

GA_TRACKING_ID = env('GA_TRACKING_ID', default='MISSING')
USE_GA = env('DJANGO_USE_GA', default='False')
USE_GA = {'True': True, 'False': False}.get(USE_GA, False)


# Celery config
CELERY_BROKER_URL = env('CLOUDAMQP_URL', default='amqp://')
CELERY_BROKER_POOL_LIMIT = 1
CELERY_BROKER_HEARTBEAT = None
CELERY_BROKER_CONNECTION_TIMEOUT = 30
CELERY_TASK_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_EVENT_QUEUE_EXPIRES = 60
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_CONCURRENCY = 50
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_BACKEND = None

# Email config
ANYMAIL = {
    "MAILGUN_API_KEY": env('MAILGUN_API_KEY', default=''),
    "MAILGUN_SENDER_DOMAIN": env('MAILGUN_SENDING_DOMAIN', default=''),
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "team@codesponsor.io"

# Allauth config
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}
