Virtual Environments
--------------------

Virtual environments are encapsulated python binaries. That's actually all.

Why virtual environments?
*************************

The simple answer is: Because we can.

The more complex answer is:

Most of us are working on different projects with a variety of dependencies and dependencies of dependencies. Since
we mostly are going to use different ``pypi packages`` with specific dependencies (most of the time in a specific version)
in different projects, we will have a problem with packages and versions. This works well, as long as we can ensure
that we know what we are doing. But to be honest, who knows all dependencies and their versions of our projects
anymore?

How does it work then?
**********************

In detail, your bash or shell has paths in the ``$PATH`` variable. The ``$PATH`` is the operating system's default
paths, to look for binaries, when a command is executed.

If a virtual environment is active, this path is manipulated. As an example we will check
what the OSX default ``$PATH`` looks like and a ``$PATH`` with an active virtual environment.

.. code-block:: bash

    $: echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin

    $: pipenv shell && echo $PATH
    /Users/dominik/.local/share/virtualenvs/django-demo-HpdBQ9X5/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin:/usr/local/sbin


If we look ak our default python3 binary on osx, we will find an alias in /usr/local/bin that is pointing to the
OSX Cellar path. And we will check what the structure looks there.

.. code-block:: bash

    $: ls -la /usr/local/bin | grep python3
    -rwxr-xr-x    1 root     admin       247 Sep 13  2018 ipython3
    -rwxr-xr-x    1 dominik  admin       255 Sep  6  2018 ptipython3
    -rwxr-xr-x    1 dominik  admin       254 Sep  6  2018 ptpython3
    lrwxr-xr-x    1 dominik  admin        36 Feb 27 16:42 python3 -> /usr/local/Cellar/python/3.7.2_2/bin/python3
    lrwxr-xr-x    1 dominik  admin        43 Feb 27 16:42 python3-config -> /usr/local/Cellar/python/3.7.2_2/bin/python3-config
    lrwxr-xr-x    1 dominik  admin        38 Feb 27 16:42 python3.7 -> /usr/local/Cellar/python/3.7.2_2/bin/python3.7
    lrwxr-xr-x    1 dominik  admin        45 Feb 27 16:42 python3.7-config -> /usr/local/Cellar/python/3.7.2_2/bin/python3.7-config
    lrwxr-xr-x    1 dominik  admin        39 Feb 27 16:42 python3.7m -> /usr/local/Cellar/python/3.7.2_2/bin/python3.7m
    lrwxr-xr-x    1 dominik  admin        46 Feb 27 16:42 python3.7m-config -> /usr/local/Cellar/python/3.7.2_2/bin/python3.7m-config

    $: tree /usr/local/Cellar/python/3.7.2_2/bin
    /usr/local/Cellar/python/3.7.2_2/bin
    ├── 2to3 -> ../Frameworks/Python.framework/Versions/3.7/bin/2to3
    ├── 2to3-3.7 -> ../Frameworks/Python.framework/Versions/3.7/bin/2to3-3.7
    ├── easy_install-3.7
    ├── idle3 -> ../Frameworks/Python.framework/Versions/3.7/bin/idle3
    ├── idle3.7 -> ../Frameworks/Python.framework/Versions/3.7/bin/idle3.7
    ├── pip3
    ├── pip3.7
    ├── pydoc3 -> ../Frameworks/Python.framework/Versions/3.7/bin/pydoc3
    ├── pydoc3.7 -> ../Frameworks/Python.framework/Versions/3.7/bin/pydoc3.7
    ├── python3 -> ../Frameworks/Python.framework/Versions/3.7/bin/python3
    ├── python3-config -> ../Frameworks/Python.framework/Versions/3.7/bin/python3-config
    ├── python3.7 -> ../Frameworks/Python.framework/Versions/3.7/bin/python3.7
    ├── python3.7-config -> ../Frameworks/Python.framework/Versions/3.7/bin/python3.7-config
    ├── python3.7m -> ../Frameworks/Python.framework/Versions/3.7/bin/python3.7m
    ├── python3.7m-config -> ../Frameworks/Python.framework/Versions/3.7/bin/python3.7m-config
    ├── pyvenv -> ../Frameworks/Python.framework/Versions/3.7/bin/pyvenv
    ├── pyvenv-3.7 -> ../Frameworks/Python.framework/Versions/3.7/bin/pyvenv-3.7
    └── wheel3

As expected, we found a complete set of python and helper binaries, like pip3 and pyenv. This is still our default
python binaries, mostly provided by the OS or installed manually, on OSX via ``brew``.

In our example ``pipenv`` is used and by default pipenv does create a new python binary path and files into the
users home directory. If we look at the directory now, we should see the typical python structure.

.. code-block:: bash

    $: tree /Users/dominik/.local/share/virtualenvs/django-demo-HpdBQ9X5/bin
    ├── activate
    ├── activate.csh
    ├── activate.fish
    ├── activate_this.py
    ├── chardetect
    ├── cm2html
    ├── cm2latex
    ├── cm2man
    ├── cm2pseudoxml
    ├── cm2xetex
    ├── cm2xml
    ├── cmark
    ├── django-admin
    ├── django-admin.py
    ├── easy_install
    ├── easy_install-3.7
    ├── futurize
    ├── pasteurize
    ├── pip
    ├── pip3
    ├── pip3.7
    ├── pybabel
    ├── pygmentize
    ├── python -> python3.7
    ├── python-config
    ├── python3 -> python3.7
    ├── python3.7
    ├── rst2html.py
    ├── rst2html4.py
    ├── rst2html5.py
    ├── rst2latex.py
    ├── rst2man.py
    ├── rst2odt.py
    ├── rst2odt_prepstyles.py
    ├── rst2pseudoxml.py
    ├── rst2s5.py
    ├── rst2xetex.py
    ├── rst2xml.py
    ├── rstpep2html.py
    ├── sphinx-apidoc
    ├── sphinx-autogen
    ├── sphinx-build
    ├── sphinx-quickstart
    ├── sqlformat
    └── wheel

And again, as expected, there are all installed binaries for this virtual environment. We already can see a difference
in packages (binaries) included.

To wrap this conclusion up, the OS ``$PATH`` variable evaluate which python binary should be used. The OS (as I
understood it), does lookup every path in the ``$PATH`` variable and looks for a binary that matches the commands name.
If the binary, according to the command name, has been found, it will execute this.

So, for us this means, whatever is written in the ``$PATH``, we need to make sure that the virtual environment path is
listed before the default binary path. **BUT we do not have to care about this, since** ``virtualenv`` **or**
``pipenv`` **is doing this for us.**

**But don't start to mix these two options**, it will cause just issues. It's theoretical possible, but some tests
showed it's not good practice.

How to use a virtual environment?
*********************************

pipenv
......

With ``pipenv`` it is quite straight forward. All we need is an empty ``Pipfile`` in the directory we are working in,
mostly in the root directory of the project.

We then do create a new virtual environment with the command ``pipenv install``. This does create all necessary things
we need further on. By default, we have no pypi packages installed. From here on we can easily install packages with
``pipenv install django djangrestrframework``. This will create a ``Pipfile.lock`` which is a representation of the
installed pypi packages with their version and dependencies.

In a team environment, we would commit both those files to the repository. So every team member can then just run
``pipenv install`` to install all dependencies.

To activate the environment, we can simply use ``pipenv shell``. Now the virtual environment is active and we can
use the bash or shell normally, as we do normally. An indication for an active virtual environment is the prefix
of the bash or shell like this ``django-demo-HpdBQ9X5 > ~/dev/django-demo/docs`` compared to a normal bash
``~/dev/django-demo`` prefix.

Another way how to interact with the pipenv virtual environment is the ``pipenv run`` command. This command allows
us to use the virtual environment without activating it. For example ``pipenv run apps/manage.py migrate``.

To deactivate the ``pipenv shell`` you have to use the command ``deactivate``.

The ``requirements.txt`` file can be used initially to transfer your current structure into pipenv with running
``pipenv install -r requirements.txt``. This will transfer everything into the ``Pipfile`` and further on this
can be used.

I realized it is very helpful for CI with circleci, because we don't need to activate anything before we want to run
the with pytest. Saved one line of code there..


virtualenv
..........

If we want to use ``virtualenv`` we create a with the command ``virtualenv .venv``. The second parameter is the
directory where the python binary structure will be placed. Usually the community is using ``.venv`` or ``.env``.

With virtualenv we don't have an option to run a command within the virtual environment without activating it. There
is one option, to run the python binaries with the virtual environment directly, but that is very bad practice,
because we have to assume everybody has their path at another path.

So, we will want to activate it with ``source .venv/bin/activate``. With the virtual environment active, we can use
the bash as usually.

As in with pipenv, to deactivate virtual environment you have to use the command ``deactivate``.

A big disadvantage of ``virtualenv``, it doesn't keep track of your dependencies automatically. You must output
the pypi packages with ``pip freeze`` and then manually copy and paste it to your ``requirements.txt`` file(s).
