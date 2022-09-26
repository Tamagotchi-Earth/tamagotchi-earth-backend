import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class UUIDFilenameGenerator:
    """Filename generator for obfuscating FileField/ImageField filenames with UUIDv4"""

    def __init__(self, basepath: str):
        self._basepath = basepath

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]
        return os.path.join(self._basepath, f'{uuid4().hex}{ext}')
