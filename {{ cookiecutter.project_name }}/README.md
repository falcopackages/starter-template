# {{ cookiecutter.project_name }}

[![falco](https://img.shields.io/badge/built%20with-falco-success)](https://github.com/falcopackages/falco)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)

## Development

### Setup project

```shell
just setup
```
Read the content of the justfile to understand what this command does. Essentially, it sets up your virtual environment, 
installs the dependencies, runs migrations, and creates a superuser with the credentials `admin@localhost` (email) and `admin` (password).

### Run the django development server

```shell
just server
```

### Run django commands

The simple way to run any django command, without having to activate your virtualenv is using the `dj` recipe, for example:

```shell
just dj migrate
```

You'll notice that contrary to a typical django project there is no `manage.py` file. The content that is usually in that file has been moved to `{{ cookiecutter.project_name }}/__main__.py`. 
Instead of running `python manage.py command`, you can run (while your virtualenv is activated):

```shell
source .venv/bin/activate
python -m {{ cookiecutter.project_name }} migrate
python {{ cookiecutter.project_name }} runserver # -m is optional
{{ cookiecutter.project_name }} runserver
```

> [!TIP]
> Run `just` to see all available commands.
