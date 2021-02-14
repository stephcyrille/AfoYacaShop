from django import template

register = template.Library()


@register.filter()
def get_single_variety_pictures(list_, value):
    return list_[value].get_pictures()
