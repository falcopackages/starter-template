Authentication
==============

Login Required
---------------

The `LoginRequiredMiddleware <https://docs.djangoproject.com/en/5.1/ref/middleware/#module-django.contrib.auth.middleware>`_ is enabled to make all views require login
by default. To make a view public, you use the `@login_not_required <https://docs.djangoproject.com/en/5.1/topics/auth/default/#django.contrib.auth.decorators.login_not_required>`_ decorator.

.. code-block:: python
    :caption: Example

    from django.contrib.auth.decorators import login_not_required

    @login_not_required
    def public_view(request):
        return HttpResponse("This is a public view")


Login via email instead of username
-----------------------------------

The ``email`` field is configured as the login field using a custom ``EmailBackend`` in the ``accounts`` app.
The ``User`` model still has a ``username`` field, but it is auto-generated from the email address on signup
to minimize friction.

Brute-force Protection
----------------------

`django-axes <https://github.com/jazzband/django-axes>`_ is enabled to track login attempts and block
brute-force attacks. It's configured to track the client IP address in addition to the username.

Password Reset
--------------

Standard Django password reset views are included in the ``accounts`` app. Password reset emails
are sent via Amazon SES (in production) or the console (in development).

.. admonition:: Custom user model
    :class: note dropdown

     Falco does not ship with a custom user model. There are great resources on why this is often the best approach:

     - https://noumenal.es/posts/django-unique-user-email/928/
     - https://buttondown.com/carlton/archive/evolving-djangos-authuser/

     If you need to save user data, a profile model is a better approach, and better field names are ``full_name`` and ``short_name``.
