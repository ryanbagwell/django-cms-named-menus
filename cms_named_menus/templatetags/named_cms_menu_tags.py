from menus.templatetags.menu_tags import ShowMenu
from classytags.arguments import IntegerArgument, Argument, StringArgument
from classytags.core import Options
from django import template
from ..models import CMSNamedMenu
from django.core.exceptions import ObjectDoesNotExist
import logging
from menus.menu_pool import menu_pool
from cms.api import get_page_draft
from cms.utils.moderator import use_draft
from cms.models.pagemodel import Page
try:
    from cms.menu import page_to_node
except ImportError:
    from cms.cms_menus import page_to_node

logger = logging.getLogger(__name__)

register = template.Library()


class ShowMultipleMenu(ShowMenu):
    name = 'show_named_menu'

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

        context.update({'children': [],
                        'template': kwargs.get('template'),
                        'from_level': kwargs.get('from_level'),
                        'to_level': kwargs.get('to_level'),
                        'extra_inactive': kwargs.get('extra_inactive'),
                        'extra_active': kwargs.get('extra_active'),
                        'namespace': kwargs.get('namespace')
                        })

        try:
            named_menu = CMSNamedMenu.objects.get(name__iexact=menu_name).pages
        except ObjectDoesNotExist:
            logging.warn("Named CMS Menu %s not found" % menu_name)
            return context

        nodes = menu_pool.get_nodes(context['request'], kwargs['namespace'], kwargs['root_id'])

        context.update({
            'children': self.arrange_nodes(nodes, named_menu, namespace=kwargs['namespace'])
        })

        return context

    def arrange_nodes(self, node_list, node_config, namespace=None):
        
        arranged_nodes = []

        for item in node_config:
            item.update({'namespace': namespace})
            node = self.create_node(item, node_list)
            if node is not None:
                arranged_nodes.append(node)

        return arranged_nodes

    def create_node(self, item, node_list):
        
        item_node = self.get_node_by_id(item['id'], node_list, namespace=item['namespace'])
        if item_node is None:
            return None
        
        for child_item in item.get('children', []):
            
            child_node = self.get_node_by_id(child_item['id'], node_list, namespace=item['namespace'])
            if child_node is not None:
                item_node.children.append(child_node)

        return item_node

    def get_node_by_id(self, id, nodes, namespace=None):

        final_node = None

        try:
            for node in nodes:
                
                if node.id == id:
                    if namespace:
                        if node.namespace == namespace:
                            final_node = node
                            break
                    else:
                        final_node = node
                        break
    
            if final_node is None:

                """ If we're editing a page, we need to find
                    the draft version of the page and turn it
                    into a navigation node """

                page = get_page_draft(Page.objects.get(id=id))

                final_node = page_to_node(page, page, 0)

            final_node.children = []
            final_node.parent = []
        except:
            logger.exception('Failed to find node')

        return final_node


register.tag(ShowMultipleMenu)
