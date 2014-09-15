from django.contrib import admin
from .models import CMSNamedMenu
from cms.models.pagemodel import Page
from collections import OrderedDict
import json
from django.conf import settings


class CMSNamedMenuAdmin(admin.ModelAdmin):
    change_form_template = 'cms_named_menus/change_form.html'

    readoly_fields = ('pages_json',)

    def change_view(self, request, object_id, form_url='', extra_context={}):

        menu = CMSNamedMenu.objects.get(id=object_id).pages_json

        extra_context = {
            'menu_pages': json.dumps(menu),
            'cms_pages': self.get_pages_json(),
            'debug': settings.DEBUG,
        }

        return super(CMSNamedMenuAdmin, self).change_view(request, object_id, form_url, extra_context)

    def get_pages_json(self):

        pages_json = []

        pages = Page.objects.all()

        for page in pages:

            pages_json.append({
                'title': page.get_title(),
                'slug': page.get_slug(),
                'id': page.id,
            })

        return json.dumps(pages_json)


admin.site.register(CMSNamedMenu, CMSNamedMenuAdmin)

