import socket
import environ

root = environ.Path(__file__) - 2  # Set the base directory to two levels
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
    'home',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
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
]

ROOT_URLCONF = env('ROOT_URLCONF', default='code_sponsor.urls')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root.path('templates')],
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



# AWS
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='MISSING')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='MISSING')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='codesponsor')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
STATICFILES_DIRS = env.tuple('STATICFILES_DIRS', default=('assets/', ))
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'app.storages.S3HashedStorage'

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

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

GA_TRACKING_ID = env('GA_TRACKING_ID', default='MISSING')
USE_GA = env('DJANGO_USE_GA', default='False')
USE_GA = {'True': True, 'False': False}.get(USE_GA, False)
