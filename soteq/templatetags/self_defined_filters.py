from django import template

register = template.Library()

@register.filter(name='iternum')
def iternum(num):
    return range(num)
