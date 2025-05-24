from django import template

register = template.Library()

@register.filter
def currency_vnd(value):
    try:
        value = float(value)
        return f"{value:,.0f}₫".replace(",", ".")
    except (ValueError, TypeError):
        return value
