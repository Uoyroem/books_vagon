from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment
import django_bootstrap5.forms


def environment(**options):
    environment = Environment(**options)
    environment.globals.update(
        {
            "static": static,
            "url": reverse,
            "bootstrap_form": django_bootstrap5.forms.render_form,
        }
    )
    return environment
