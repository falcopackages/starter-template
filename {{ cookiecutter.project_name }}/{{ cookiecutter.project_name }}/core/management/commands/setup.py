from contextlib import suppress

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Run project setup tasks, applying migrations, creating a superuser if needed etc."

    def handle(self, *_, **__):
        call_command("litestream", "--skip-checks", "init")
        call_command(
            "litestream",
            "--skip-checks",
            "restore",
            "default",
            "-if-replica-exists",
            "-if-db-not-exists",
        )
        call_command("migrate", "--skip-checks")
        call_command("setup_periodic_tasks", "--skip-checks")
        with suppress(CommandError):
            call_command("createsuperuser", "--skip-checks", "--noinput", "--traceback")
