from django import template

register = template.Library()

def cut(value,arg):
    """
    Basically replaces value with WARNING
    """
    return value.replace(arg,'')



register.filter('cut',cut)
