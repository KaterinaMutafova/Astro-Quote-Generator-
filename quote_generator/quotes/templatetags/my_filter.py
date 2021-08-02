from django import template



register = template.Library()


@register.filter(name="quotation_marks")
def quotation_marks(value):
    return "\"" + value + "\""











