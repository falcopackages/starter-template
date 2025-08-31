from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any

from datastar_py import ServerSentEventGenerator as SSE
from datastar_py.django import DatastarResponse
from django import forms
from django.conf import settings
from django.core.paginator import InvalidPage
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import QuerySet
from django.http import Http404
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse


def paginate_queryset(
    request: HttpRequest,
    queryset: QuerySet,
    page_size: int = settings.DEFAULT_PAGE_SIZE,
):
    paginator = Paginator(queryset, page_size)
    page_number = request.GET.get("page") or 1
    try:
        page_number = int(page_number)
    except ValueError as e:
        if page_number == "last":
            page_number = paginator.num_pages
        else:
            msg = "Page is not 'last', nor can it be converted to an int."
            raise Http404(msg) from e

    try:
        return paginator.page(page_number)
    except InvalidPage as exc:
        msg = "Invalid page (%s): %s"
        raise Http404(msg % (page_number, str(exc))) from exc



