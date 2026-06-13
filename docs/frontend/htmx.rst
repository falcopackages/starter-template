HTMX and Cotton Components
==========================

The project comes set up with django-cotton_ and htmx_ for when you need to add some
interactivity to your web app. `django-cotton <https://django-cotton.com/>`_ enables reusable
component-based templates right in Django.

.. admonition:: jetbrains extensions
    :class: tip dropdown

    If you are using a jetbrains IDE, there is an extension that add support for htmx, you can find it `here <https://plugins.jetbrains.com/plugin/20588-htmx-support>`_.
    There is also `this extension <https://plugins.jetbrains.com/plugin/15251-alpine-js-support>`_ for `alpinejs <https://alpinejs.dev/>`_  support.

Let's look at a quick example:

.. code-block:: django
   :linenos:
   :caption: elements.html


   {% block main %}
   <ul id="element-list">
      {% for el in elements %}
         <li>{{ el }}</li>
      {% endfor %}
   </ul>

   <form
   hx-post="{% url 'add_element' %}"
   hx-target="#element-list"
   hx-swap="beforeend"
   >
      {% csrf_token %}
      {{ form }}
      <button type="submit">Add Element</button>
   </form>

   {% endblock main %}

The htmx attributes (prefixed with ``hx-``) defined above basically say:

 when the form is submitted, make an asynchronous JavaScript request to the URL ``{% url 'add_element' %}`` and add the content of the response before the end (before the last child) element of the element with the ID ``element-list`` .

The complementary Django code on the backend would look something like this:

.. code-block:: python
   :linenos:
   :caption: views.py

   def add_element(request):
      new_element = add_new_element(request.POST)
      if request.htmx:
         return render(request, "myapp/elements.html", {"elements": [new_element]})
      else:
         redirect("elements_list")

The ``htmx`` attribute on the ``request`` element is provided by django-htmx_, which is already configured in the project.

This example illustrates how you can create a button that adds a new element to a list of elements on a page without reloading the entire page.
Although this might not seem particularly exciting, the `interactive user interfaces guide <https://falco.oluwatobi.dev/guides/interactive_user_interfaces.html>`_ provides more
practical examples that demonstrate the extensive possibilities offered by this approach.


.. _django-cotton: https://django-cotton.com/
.. _htmx: https://htmx.org/
.. _django-htmx: https://github.com/adamchainz/django-htmx