# arkhyz_life/catalog/templatetags/catalog_extras.py
from django import template
import re

register = template.Library()

@register.filter(name='filter_phone')
def filter_phone(value):
    # Удаляем все, кроме цифр и знака +
    return re.sub(r'[^\d+]', '', value)