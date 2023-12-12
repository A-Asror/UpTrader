from django import template

from ..models import MenuModel

register = template.Library()


@register.inclusion_tag("menu.html")
def draw_menu(menu_id=None, menu_name=None):
    if menu_name:
        menu_item = MenuModel.objects.filter(parent__url=menu_name).prefetch_related('children')
        return {'list_menu': menu_item}
    if menu_id is not None:
        menu_item = MenuModel.objects.prefetch_related('children').get(id=menu_id)
        return {'list_menu': [menu_item]}
    else:
        menu_items = MenuModel.objects.filter(parent__isnull=True).prefetch_related('children')
        return {'list_menu': menu_items}
