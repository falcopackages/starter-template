import multiprocessing
import subprocess
import sys
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from environs import Env

env = Env()


class Command(BaseCommand):
    help = "Run Granian as the WSGI server. If using SQLite as the database, Litestream is used for replication."

    def add_arguments(self, parser):
        parser.add_argument("--port", "-p", type=int, default=8000)
        parser.add_argument("--host", type=str, default="0.0.0.0")  # noqa
        parser.add_argument("--workers", "-w", type=int, default=multiprocessing.cpu_count() * 2 + 1)

    def handle(self, *_, **options):
        granian_args = [
            "--workers",
            str(options["workers"]),
            "--port",
            str(options["port"]),
            "--host",
            options["host"],
            "--interface",
            "wsgi",
            "blaze.wsgi:application",
        ]
        if use_litestream():
            # Construct the Granian command as a single string for Litestream
            execute_granian = f"granian {' '.join(granian_args)}"
            call_command("litestream", "--skip-checks", "replicate", "-exec", execute_granian)
        else:
            granian_executable = Path(sys.executable).parent / "granian"
            command = [str(granian_executable), *granian_args]
            subprocess.run(command, check=False)


def use_litestream() -> bool:
    return settings.DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3" and env.bool("USE_LITESTREAM", True)
