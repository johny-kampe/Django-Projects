from django import template

register = template.Library()

def myFilter(value):
    return value + " This is a string fro custom filtera"

register.filter('customFilter', myFilter)
