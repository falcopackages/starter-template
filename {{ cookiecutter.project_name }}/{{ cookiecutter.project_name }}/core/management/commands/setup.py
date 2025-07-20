from contextlib import suppress

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from .prodserver import use_litestream


class Command(BaseCommand):
    help = "Run project setup tasks, applying migrations, creating a superuser if needed etc."

    def handle(self, *_, **__):
        if use_litestream():
            call_command("litestream", "--skip-checks", "init")
            call_command(
                "litestream",
                "--skip-checks",
                "restore",
                "default",
                "-if-replica-exists",
                "-if-db-not-exists",
            )
        call_command("tailwind", "--skip-checks", "build")
        call_command("collectstatic", "--skip-checks", "--no-input")
        call_command("migrate", "--skip-checks")
        call_command("migrate", "--skip-checks", "--database", "tasks_db")
        with suppress(CommandError):
            call_command("createsuperuser", "--skip-checks", "--noinput", "--traceback")
