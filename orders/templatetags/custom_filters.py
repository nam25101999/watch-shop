from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def sum_total_price(items):
    try:
        return sum(item.quantity * item.price for item in items)
    except Exception:
        return 0
