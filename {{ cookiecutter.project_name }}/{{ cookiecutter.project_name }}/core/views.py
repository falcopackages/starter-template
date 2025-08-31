from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.auth.decorators import login_not_required
from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_GET
@cache_control(
    max_age=0 if settings.DEBUG else settings.CACHE_TIME_ROBOTS_TXT,
    immutable=True,
    public=True,
)
@login_not_required
def robots_txt(request: HttpRequest) -> HttpResponse:
    return render(request, "robots.txt", content_type="text/plain")


@require_GET
@cache_control(
    max_age=0 if settings.DEBUG else settings.CACHE_TIME_SECURITY_TXT,
    immutable=True,
    public=True,
)
@login_not_required
def security_txt(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        ".well-known/security.txt",
        context={
            "year": timezone.now().year + 1,
        },
        content_type="text/plain",
    )


@require_GET
@cache_control(
    max_age=0 if settings.DEBUG else settings.CACHE_TIME_FAVICON,
    immutable=True,
    public=True,
)
@login_not_required
def favicon(request: HttpRequest) -> HttpResponse | FileResponse:
    name = request.path.lstrip("/")
    if path := finders.find(name):
        return FileResponse(Path(path).read_bytes())
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            '<text y=".9em" font-size="90">🚀</text>'
            "</svg>"
        ),
        content_type="image/svg+xml",
    )
