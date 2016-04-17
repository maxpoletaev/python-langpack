from setuptools import setup

packages = [
    'langpack',
    'langpack.contrib.django',
    'langpack.contrib.django.templatetags',
]

setup(
    name='langpack',
    packages=packages,
    version='1.0.0',
    author='Max Poletaev',
    author_email='max.poletaev@gmail.com',
)
