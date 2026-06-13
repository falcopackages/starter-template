:description: The packages and tools that comes included with a project generated with falco.

Packages and Tools
==================

Non exhaustive list of packages and tools that comes included with your project.

System Requirements
-------------------

- `uv <https://docs.astral.sh/uv/>`_: Used for managing the project's virtual environment and dependencies, more details can be found in the `dependency management guide </dependency_management.html>`_.
- `just <https://just.system>`_: A script runner that simplifies the execution of common tasks, such as setting up the project, running the server, and running tests, run ``just`` to see all available commands.

Base Dependencies
-----------------

- `environs <https://github.com/sloria/environs>`_: Used for configuring settings via environment variables.
- `django-axes <https://github.com/jazzband/django-axes>`_: Handles login attempt tracking and brute-force protection.
- `django-template-partials <https://github.com/carltongibson/django-template-partials>`_: Used for defining reusable fragments of HTML.
- `django-htmx <https://github.com/adamchainz/django-htmx>`_: Used for making AJAX requests and updating the DOM.
- `django-lifecycle <https://github.com/rsinger86/django-lifecycle>`_: Provides an alternative to signals for hooking into your model's lifecycle.
- `django-heath-check <https://github.com/revsys/django-health-check>`_: Provides a ``/health`` endpoint for application, database, storage, and other health checks.
- `django-extensions <https://django-extensions.readthedocs.io/en/latest/>`_: Adds some useful management commands to Django, such as ``shell_plus`` and ``show_urls``.
- `django-anymail <https://github.com/anymail/django-anymail>`_: `Amazon SES <https://aws.amazon.com/ses/?nc1=h_ls>`_ is used for production email, facilitated by Anymail.
- `django-unique-user-email <https://github.com/carltongibson/django-unique-user-email>`_: Adds a unique constraint to the email field of the Django ``User`` model.
- `django-tasks-db <https://github.com/RealOrangeOne/django-tasks>`_: Database-backed task queue and scheduling.
- `django-litestream <https://github.com/Tobi-De/django-litestream/>`_: Provides SQLite replication and backup if you choose to use SQLite in production.
- `django-storages <https://django-storages.readthedocs.io/en/latest/>`_: Used for storing media files on AWS S3.
- `diskcache <https://github.com/grantjenks/python-diskcache>`_: A simple and fast cache solution based on ``sqlite3``, just add a ``LOCATION`` environnment folder for the cache location and you are good to go.
- `Docker <https://www.docker.com/>`_ and `s6-overlay <https://github.com/just-containers/s6-overlay>`_: Docker is configured for production, with s6-overlay enabling running both the web server process (``granian``) and the background worker process (``django-tasks-db``) within a single container.
- `granian <https://github.com/emmett-framework/granian>`_: Used a the production web server.
- `Sentry <https://sentry.io/welcome/>`_: Utilized for performance and error monitoring.
- `Whitenoise <https://whitenoise.evans.io/en/latest/>`_: Used to serve static files.
- `heroicons <https://heroicons.com/>`_: Easy access to `heroicons <https://heroicons.com/>`_ in your Django templates.
- `django-cotton <https://github.com/wrabit/django-cotton>`_: Cotton components for reusable UI.

Development-Only packages
-------------------------

- `django-debug-toolbar <https://django-debug-toolbar.readthedocs.io/en/latest/>`_: Of course, a must.
- `django-browser-reload <https://github.com/adamchainz/django-browser-reload>`_: Automatically reloads your browser on code changes in development.
- `django-watchfiles <https://github.com/adamchainz/django-watchfiles>`_: Faster and more efficient development server reloading.
- `django-fastdev <https://github.com/boxed/django-fastdev>`_: Helps catch small mistakes early in your project.
- `dj-notebook <https://github.com/pydanny/dj-notebook>`_: Allows you to use your shell_plus in a Jupyter notebook.
- `pytest <https://docs.pytest.org/en/7.0.x/>`_: Used for running tests
- `pytest-django <https://pytest-django.readthedocs.io/en/latest/>`_: Pytest plugin for Django.
- `pytest-sugar <https://github.com/Teemu/pytest-sugar>`_: Better looking pytest output.
- `pytest-xdist <https://github.com/pytest-dev/pytest-xdist>`_: Run tests in parallel.
- `Werkzeug <https://werkzeug.palletsprojects.com/en/2.1.x/>`_: Enable the Werkzeug debugger when running `manage.py runserver_plus`.
- `falco-cli <https://github.com/falcopackages/falco-cli>`_: CLI for CRUD generation, project scaffolding, and Django utilities.

CSS Frameworks
--------------

- `django-tailwind-cli <https://github.com/oliverandrich/django-tailwind-cli>`_: Integration with tailwind css using the `Tailwind CSS CLI <https://tailwindcss.com/blog/standalone-cli>`_, eliminating the need for Node.js.

Extra Tools
-----------

Additional tools that are not installed directly in the project environment but are invoked via `uv tool <https://docs.astral.sh/uv/guides/tools/>`_:

- `pre-commit <https://github.com/pre-commit/pre-commit>`_: Code quality and linting tool that runs before every commit.
- `git-cliff <https://git-cliff.org/>`_: Generates a changelog based on your commit messages and the `conventional commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ format.
- `bump-my-version <https://github.com/callowayproject/bump-my-version>`_: Bumps the version of your project following the `semver <https://semver.org/>`_ format.


Recommended
-----------

Here's a list of extra packages I use from time to time that don't come included in the starter-template:

- `django-tomselect <https://github.com/OmenApps/django-tomselect>`_
- `django-simple-nav <https://github.com/westerveltco/django-simple-nav>`_
- `django-tables2 <https://github.com/jieter/django-tables2>`_
- `django-pgtrigger <https://github.com/Opus10/django-pgtrigger>`_
- `django-eventstream <https://github.com/fanout/django-eventstream>`_
- `django-pgclone <https://github.com/Opus10/django-pgclone>`_
- `django-perf-rec <https://github.com/adamchainz/django-perf-rec>`_
- `coltrane <https://github.com/adamghill/coltrane>`_
