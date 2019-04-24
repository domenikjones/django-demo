Django Project Setup
====================

The django management commands provide us commands to start a new django project with few commands. Some commands
you will need when you create a new Django app:


.. code-block:: bash

    $: pipenv install django
    $: pipenv run django-admin startproject src
    [..]
    $: pipenv run src/manage.py migrate
    $: pipenv run src/manage.py createsuperuser
    $: pipenv run src/manage.py runserver 0.0.0.0:8080


After we created the project with the ``startporject [name]`` command, we do rearrange some files and imports, so
it will fit our project structure. This is not necessary, but recommended.


.. code-block:: bash

    .
    ├── .circleci
    │   └── config.yml
    ├── .gitignore
    ├── Makefile
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── docker-compose.yml
    ├── docs
    ├── research
    └── src
        ├── apps
        │   ├── api
        │   └── core
        │       ├── admin.py
        │       ├── models.py
        │       ├── serialiers.py
        │       └── view.py
        ├── conf
        │   ├── base.py
        │   ├── local.py
        │   └── staging.py
        ├── manage.py
        ├── requirements
        │   ├── base.txt
        │   ├── local.txt
        │   └── staging.txt
        ├── settings.py
        └── urls.py

