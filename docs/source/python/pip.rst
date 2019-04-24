PIP
---

pip is a ``package-management system`` used to install and manage software packages written in Python. Many packages
can be found in the default source for packages and their dependencies [#]_.

Examples how to use pip commands with ``version matching``:


.. code-block:: bash

    $: pip install django
    $: pip install django==2.2.5
    $: pip install django<=2.3
    $: pip install django>=2.2,<3

    $: pip freeze
    [..]
    chardet==3.0.4
    commonmark==0.8.1
    Django==2.2
    django-filter==2.1.0
    django-grappelli==2.12.2
    [..]


requirements.txt
................


To provide a list a packages to install (with or without versions) we can create a `requirements.txt` file. We can use
it in a way to support our dev-tier deployment strategy.

We can reference another `*.txt` file in our requirements.txt file. A good idea is to create a `base.txt` file, this
contains all dependencies needed to run the application at it's minimum, like ``django`` or ``psycopg2``. Further on
you can create more files for local, develop, staging and production. It's widely spread, to have a `tests.txt` that
contains all dependencies to run the test suite.

In a practical example we would have these files:

base.txt

.. code-block:: bash

    django>=2.1,<2.3
    djangorestframework<4

tests.txt

.. code-block:: bash

    pytest
    pytest-cov
    django-pytest


local.txt

.. code-block:: bash

    -r base.txt
    -r tests.txt

    django-debugtoolbar
    django-extensions
    Werkzeug


To install pip packages with a requirements.txt you run ``pip install -r requirements/local.txt``. This will install
all dependencies and will also try to overwrite existing, maybe newer, version of a dependency.

You can then also use these files to instantiate your ``pipenv`` environment. This is an example how to us it
``pipenv install -r requirements/local.txt``. When you are using ``pipenv shell`` to activate your virtual
environment, you can simply use ``pip`` as usual.


.. [#] https://en.wikipedia.org/wiki/Pip_(package_manager).

