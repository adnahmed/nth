# nth/settings.py
from configurations import Configuration, importer

importer.install(check_options=True)

class Dev(Configuration):
    DEBUG = True