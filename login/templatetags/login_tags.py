from __future__ import unicode_literals
from django import template

register = template.Library()

#Uso en el template (if request.user|has_group_user:"Administradores")
@register.filter()
def has_group_user(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False