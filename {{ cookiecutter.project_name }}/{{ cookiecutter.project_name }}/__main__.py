import os
import sys
import multiprocessing
import subprocess
from pathlib import Path
from contextlib import suppress
from falco.manage import main, register

HOST = "0.0.0.0"
PORT = 8000
PROJECT_NAME = "{{ cookiecutter.project_name }}"
WSGI_APPLICATION = f"{PROJECT_NAME}.wsgi:application"

current_path = Path(__file__).parent.parent.resolve()
sys.path.append(str(current_path))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings")


@register("setup")
def run_setup(_):
    """
    Run project setup tasks, applying migrations, creating a superuser if needed etc.
    """
    from django.core.management import execute_from_command_line
    from django.core.management.base import CommandError

    execute_from_command_line(["manage", "litestream", "init"])
    execute_from_command_line(
        [
            "manage",
            "litestream",
            "restore",
            "default",
            "-if-replica-exists",
            "-if-db-not-exists",
        ]
    )
    execute_from_command_line(["manage", "migrate"])
    execute_from_command_line(["manage", "setup_periodic_tasks"])
    with suppress(CommandError):
        execute_from_command_line(
            ["manage", "createsuperuser", "--noinput", "--traceback"]
        )


@register("granian")
def run_granian(_):
    """
    Run Granian, the WSGI server. If using SQLite as the database, Litestream is used for replication.
    """
    bin_dir = Path(sys.executable).parent
    granian_executable = bin_dir / "granian"

    workers = multiprocessing.cpu_count() * 2 + 1
    granian_args = [
        "--workers",
        str(workers),
        "--interface",
        "wsgi",
        "--port",
        str(PORT),
        "--host",
        HOST,
        WSGI_APPLICATION,
    ]

    if "sqlite" in os.getenv("DATABASE_URL", ""):
        # Construct the Granian command as a single string for Litestream
        litestream_executable = bin_dir / "litestream"
        execute_granian = f"granian {' '.join(granian_args)}"
        command = [str(litestream_executable), "replicate", "-exec", execute_granian]
    else:
        command = [str(granian_executable)] + granian_args

    subprocess.run(command, check=True)


@register("qcluster")
def run_qcluster(argv) -> None:
    """
    Run the Django Q cluster for handling background tasks.
    """
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage", "qcluster", *argv[2:]])


if __name__ == "__main__":
    main(default_command="granian")
