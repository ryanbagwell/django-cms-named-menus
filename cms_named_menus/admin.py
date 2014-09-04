from django.contrib import admin
from .models import NamedCMSMenu
from cms.models.pagemodel import Page
from collections import OrderedDict
import json


class NamedCMSMenuAdmin(admin.ModelAdmin):
    change_form_template = 'named_cms_menus/change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context={}):

        extra_context['menu_pages'] = NamedCMSMenu.objects.get(id=object_id).pages_json

        extra_context['cms_pages'] = self.get_pages_json()

        return super(NamedCMSMenuAdmin, self).change_view(request, object_id, form_url, extra_context)

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








admin.site.register(NamedCMSMenu, NamedCMSMenuAdmin)

