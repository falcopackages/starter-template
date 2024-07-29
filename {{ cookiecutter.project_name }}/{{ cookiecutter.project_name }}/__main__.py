import multiprocessing
import os
import sys

from gunicorn.app import wsgiapp


def main() -> None:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings"
    )

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
    """
    Run gunicorn the wsgi server.
    https://docs.gunicorn.org/en/stable/settings.html
    https://adamj.eu/tech/2021/12/29/set-up-a-gunicorn-configuration-file-and-test-it/
    """

    workers = multiprocessing.cpu_count() * 2 + 1
    gunicorn_args = [
        "{{ cookiecutter.project_name }}.wsgi:application",
        "--bind",
        "127.0.0.1:8000",
        # "unix:/run/{{ cookiecutter.project_name }}.gunicorn.sock", # uncomment this line and comment the line above to use a socket file
        "--max-requests",
        "1000",
        "--max-requests-jitter",
        "50",
        "--workers",
        str(workers),
        "--access-logfile",
        "-",
        "--error-logfile",
        "-",
    ]
    argv.extend(gunicorn_args)
    wsgiapp.run()


def run_setup(_):
    """Run some project setup tasks"""
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "migrate"])
    execute_from_command_line(["manage.py", "createsuperuser", "--noinput"])
    execute_from_command_line(["manage.py", "setup_periodic_tasks"])



COMMANDS = {"qcluster": run_qcluster, "manage": run_manage, "setup": run_setup}


if __name__ == "__main__":
    main()
