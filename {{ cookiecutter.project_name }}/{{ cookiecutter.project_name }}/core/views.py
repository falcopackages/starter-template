from __future__ import annotations

from pathlib import Path

from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

ONE_DAY = 60 * 60 * 24


@require_GET
@cache_control(max_age=ONE_DAY, immutable=True, public=True)
def robots_txt(request: HttpRequest) -> HttpResponse:
    return render(request, "robots.txt", content_type="text/plain")


@require_GET
@cache_control(max_age=ONE_DAY, immutable=True, public=True)
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
@cache_control(max_age=ONE_DAY, immutable=True, public=True)
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
