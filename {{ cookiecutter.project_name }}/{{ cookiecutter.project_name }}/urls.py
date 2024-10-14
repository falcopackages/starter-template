from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView
from falco import views as falco_views
from falco.urls import favicon_urlpatterns, errors_urlpatterns
from health_check.views import MainView
from allauth.account.decorators import secure_admin_login
from debug_toolbar.toolbar import debug_toolbar_urls

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path(".well-known/security.txt", falco_views.security_txt),
    path("robots.txt", falco_views.robots_txt),
    path("", include(favicon_urlpatterns)),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("health/", MainView.as_view()),
    path("accounts/", include("allauth.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ] + debug_toolbar_urls() + errors_urlpatterns
