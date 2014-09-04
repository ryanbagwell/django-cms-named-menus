from menus.templatetags.menu_tags import ShowMenu
from classytags.arguments import IntegerArgument, Argument, StringArgument
from classytags.core import Options
from django import template
from ..models import NamedCMSMenu
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

register = template.Library()


class ShowMultipleMenu(ShowMenu):
    name = 'show_multiple_menu'

    options = Options(
        StringArgument('menu_name', required=True),
        IntegerArgument('from_level', default=0, required=False),
        IntegerArgument('to_level', default=100, required=False),
        IntegerArgument('extra_inactive', default=0, required=False),
        IntegerArgument('extra_active', default=1000, required=False),
        StringArgument('template', default='menu/menu.html', required=False),
        StringArgument('namespace', default=None, required=False),
        StringArgument('root_id', default=None, required=False),
        Argument('next_page', default=None, required=False),
    )

    def get_context(self, context, **kwargs):

        menu_name = kwargs.pop('menu_name')

        context = super(ShowMultipleMenu, self).get_context(context, **kwargs)

        try:
            menu = NamedCMSMenu.objects.get(name__iexact=menu_name)
        except ObjectDoesNotExist:
            logging.warn("Named CMS Menu %s not found" % menu_name)
            context['children'] = []
            return context

        menu_pages = menu.get_page_titles()

        context.update({
            'children': self.filter_children(menu_pages, context['children'])
            })

        return context

    def filter_children(self, menu_pages, children):

        return [node for node in children if node.title in menu_pages]

register.tag(ShowMultipleMenu)

