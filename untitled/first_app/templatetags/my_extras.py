from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):

    #this cuts out all values of arg from string
    return value.replace(arg,'')

#register.filter('cut',cut)  #we can use this method to register or use decorators ie @and a value ones

