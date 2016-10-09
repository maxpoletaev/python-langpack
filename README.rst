.. image::
    https://travis-ci.org/zenwalker/python-langpack.svg?branch=master
    :target: https://travis-ci.org/zenwalker/python-langpack

.. image::
    https://coveralls.io/repos/github/zenwalker/python-langpack/badge.svg
    :target: https://coveralls.io/github/zenwalker/python-langpack

.. image::
  https://img.shields.io/badge/status-beta-yellow.svg


========
LangPack
========

**LangPack** — key-based localization (translation) framework for Python applications. Out of the box supports Django and storing translations in YAML files ;)

Quick Start for Django
======================

Add LangPack into your INSTALLED_APPS and configure file loaders.
**Note** you should be install pyyaml package before using YAML for translations.

.. code-block:: python

    INSTALLED_APPS = [
        'langpack.contrib.django',
    ]

    LANGPACK_LOADERS = [
        ('langpack.loaders.YamlLoader', ['yaml', 'yml']),
    ]


Create your first translation file `project/locales/mainpage.yaml` with the following content:

.. code-block:: yaml

    en:
        welcome_back: "Welcome back, {name}!"

And use it in your template file:

.. code-block:: html

    {% load trans from langpack %}
    <h1>{% trans "mainpage.welcome" name=request.user.first_name %}</h1>

You can also use translations in python files:

.. code-block:: python

    from langpack.contrib.django import trans_lazy
    from django.shortcuts import render

    def welcome_page(request):
        text = trans_lazy('mainpage.welcome_back', name=request.user.first_name)
        return render('mainpage.html', {'welcome_text': text})

LangPack is fully integrated with Django localization system. All tools, such as ``LocaleMiddleware`` or ``i18n_patterns`` works without problems. We just take current locale form builtin Django method ``get_language()``.
