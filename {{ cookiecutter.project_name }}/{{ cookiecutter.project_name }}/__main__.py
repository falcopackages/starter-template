#!/usr/bin/env python3
import os
import sys


def main():
    """Application entry point."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings")
    try:
        from django.core.management import (  # pylint: disable=import-outside-toplevel
            execute_from_command_line,
        )
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
