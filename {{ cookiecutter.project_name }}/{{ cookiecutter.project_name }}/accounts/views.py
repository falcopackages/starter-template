from django.contrib.auth import login
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from .forms import LoginForm, SignupForm


class LoginView(DjangoLoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm


@login_not_required
def signup(request: HttpRequest) -> HttpResponse:
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("home")
    return TemplateResponse(request, "accounts/signup.html", {"form": form})
