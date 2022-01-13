from django import template

register = template.Library()
@register.filter(name='index')
def index(list,value):
    return list[value]