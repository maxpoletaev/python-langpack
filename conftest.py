from django.conf import settings
import django


def pytest_configure():
    setup_django()


def setup_django():
    settings.configure(
        INSTALLED_APPS=['langpack.contrib.django'],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
        }],
    )

    django.setup()
