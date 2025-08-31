from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_not_required
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView
from django.views import defaults as default_views
from {{ cookiecutter.project_name }}.core.views import favicon
from {{ cookiecutter.project_name }}.core.views import robots_txt
from {{ cookiecutter.project_name }}.core.views import security_txt
from health_check.views import MainView

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path("android-chrome-192x192.png", favicon),
    path("android-chrome-512x512.png", favicon),
    path("apple-touch-icon.png", favicon),
    path("browserconfig.xml", favicon),
    path("favicon-16x16.png", favicon),
    path("favicon-32x32.png", favicon),
    path("favicon.ico", favicon),
    path("mstile-150x150.png", favicon),
    path("safari-pinned-tab.svg", favicon),
    path(".well-known/security.txt", security_txt),
    path("robots.txt", robots_txt),
    path("", login_not_required(TemplateView.as_view(template_name="index.html")), name="home"),
    path("health/", login_not_required(MainView.as_view())),
    path("accounts/", include("allauth.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        *debug_toolbar_urls(),
    ]
