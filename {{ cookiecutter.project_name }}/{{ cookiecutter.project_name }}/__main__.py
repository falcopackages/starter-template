import os
import sys

from gunicorn.app import wsgiapp


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmprep.settings")

    run_func = None
    if len(sys.argv) > 1:
        run_func = COMMANDS.get(sys.argv[1])

    if run_func:
        run_func(sys.argv)
    else:
        run_gunicorn(sys.argv)


def run_qcluster(argv: list) -> None:
    """Run Django-q cluster."""
    from django.core.management import execute_from_command_line

    execute_from_command_line(argv[2:])


def run_manage(argv: list) -> None:
    """Run Django's manage command."""
    from django.core.management import execute_from_command_line

    execute_from_command_line(argv[1:])


def run_gunicorn(argv: list) -> None:
    """Run the web server."""
    argv.append("{{ cookiecutter.project_name }}.wsgi:application")
    argv.append("--config")
    argv.append("gunicorn.conf.py")
    wsgiapp.run()


COMMANDS = {"qcluster": run_qcluster, "manage": run_manage}


if __name__ == "__main__":
    main()
