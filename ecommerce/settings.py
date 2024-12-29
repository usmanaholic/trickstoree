
# Django settings for ecommerce project.

#Generated by 'django-admin startproject' using Django 3.0.5.

#For more information on this file, see
#https://docs.djangoproject.com/en/3.0/topics/settings/

#For the full list of settings and their values, see
#https://docs.djangoproject.com/en/3.0/ref/settings/


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

STATIC_URL = '/static/'

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'  # URL to access uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#vw(03o=(9kbvg!&2d5i!2$_58x@_-3l4wujpow6(ym37jxnza'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecom',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'ckeditor_uploader',




]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",





]


ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'ecom.context_processors.categories_context',

            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

AUTHENTICATION_BACKENDS = [

  
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=[STATIC_DIR,]

MEDIA_ROOT=os.path.join(BASE_DIR,'static')



LOGIN_REDIRECT_URL='/afterlogin'

#for contact us give your gmail id and password
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'from@gmail.com' # this email will be used to send emails
EMAIL_HOST_PASSWORD = 'xyz' # host email password required
# now sign in with your host gmail account in your browser
# open following link and turn it ON
# https://myaccount.google.com/lesssecureapps
# otherwise you will get SMTPAuthenticationError at /contactus
# this process is required because google blocks apps authentication by default
EMAIL_RECEIVING_USER = ['to@gmail.com'] # email on which you will receive messages sent from website


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

#cilent = 684301863978-bsrhbf6cjthe3fhumlnbo422rue111ri.apps.googleusercontent.com
#client secret = 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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


PAYFAST_MERCHANT_ID = '24480'
PAYFAST_MERCHANT_KEY = 'nb-EGJllKEBs4Xfg2psRUJYy'
PAYFAST_URL = "https://www.payfast.co.za/eng/process"
PAYFAST_RETURN_URL = 'http://127.0.0.1:8000//payment_success/'
PAYFAST_CANCEL_URL = 'http://127.0.0.1:8000/payment_cancel/'
PAYFAST_NOTIFY_URL = 'http://127.0.0.1:8000/payment_notify/'


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}