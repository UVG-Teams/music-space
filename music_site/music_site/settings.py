"""
Django settings for music_site project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
sys.path.insert(1, '../')
import credentials

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ro6khv*$pvtz)&bm8p-a8)de_hy%o0swad5#lua7*yl4_7n@*p'

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

    'music_streaming.apps.MusicStreamingConfig',
    'reports.apps.ReportsConfig',
    'mongoServices.apps.MongoservicesConfig',
    'audits.apps.AuditsConfig',
    'shoppingcarts.apps.ShoppingcartsConfig',
    
    'albums.apps.AlbumsConfig',
    'artists.apps.ArtistsConfig',
    'customers.apps.CustomersConfig',
    'employees.apps.EmployeesConfig',
    'genres.apps.GenresConfig',
    'invoiceLines.apps.InvoicelinesConfig',
    'invoices.apps.InvoicesConfig',
    'mediaTypes.apps.MediatypesConfig',
    'playlists.apps.PlaylistsConfig',
    'playlistTracks.apps.PlaylisttracksConfig',
    'tracks.apps.TracksConfig',
    'userAlbums.apps.UseralbumsConfig',
    'userArtists.apps.UserartistsConfig',
    'userGenres.apps.UsergenresConfig',
    'userPlaylists.apps.UserplaylistsConfig',
    'userTracks.apps.UsertracksConfig',
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

ROOT_URLCONF = 'music_site.urls'

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

WSGI_APPLICATION = 'music_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': credentials.DATABASE['NAME'],
        'USER': credentials.DATABASE['USER'],
        'PASSWORD': credentials.DATABASE['PASSWORD'],
        'HOST': credentials.DATABASE['HOST'],
        'PORT': credentials.DATABASE['PORT'],
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
STATICFILES_DIRS = [
    
    os.path.join(BASE_DIR, 'static'),
    
]

LOGIN_URL = "/"

LOGIN_REDIRECT_URL = "home"

LOGOUT_REDIRECT_URL = "/"