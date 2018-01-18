from django.contrib.staticfiles.storage import ManifestFilesMixin

from storages.backends.s3boto3 import S3Boto3Storage


class S3HashedStorage(ManifestFilesMixin, S3Boto3Storage):
    """Define the nifty static storage using S3 and manifest files for hashing."""
    pass