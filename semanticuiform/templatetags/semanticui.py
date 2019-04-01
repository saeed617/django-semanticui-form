from django import forms
from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
def semanticui_form(form):
    return render_to_string('semanticui/form.html', {'form': form})


@register.filter
def semanticui_field(field):
    return render_to_string('semanticui/field.html', {'field': field})

