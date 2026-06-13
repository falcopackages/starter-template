from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_not_required
from django.urls import path, reverse_lazy

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", login_not_required(views.LoginView.as_view()), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", login_not_required(views.signup), name="signup"),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
            success_url=reverse_lazy("accounts:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        login_not_required(
            auth_views.PasswordResetView.as_view(
                template_name="accounts/password_reset.html",
                email_template_name="accounts/emails/password_reset_email.html",
                success_url=reverse_lazy("accounts:password_reset_done"),
            )
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        login_not_required(
            auth_views.PasswordResetDoneView.as_view(
                template_name="accounts/password_reset_done.html"
            )
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        login_not_required(
            auth_views.PasswordResetConfirmView.as_view(
                template_name="accounts/password_reset_confirm.html",
                success_url=reverse_lazy("accounts:password_reset_complete"),
            )
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        login_not_required(
            auth_views.PasswordResetCompleteView.as_view(
                template_name="accounts/password_reset_complete.html"
            )
        ),
        name="password_reset_complete",
    ),
]
