"""
Works in conjunction with settings.py 'static and media files' info
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Custom class which inherits from django storages """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ As above but for media files """
    location = settings.MEDIAFILES_LOCATION
