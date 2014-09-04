from django.db import models
from autoslug.fields import AutoSlugField
from cms.models.pagemodel import Page
from jsonfield import JSONField
import collections


class CMSNamedMenu(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(always_update=True, populate_from='name')
    pages = models.ManyToManyField(Page)
    pages_json = JSONField(blank=True, null=True,
                           load_kwargs={
                               'object_pairs_hook': collections.OrderedDict
                           })

    def __unicode__(self):
        return self.name

    def get_page_titles(self):
        pages = self.pages.all()
        return [page.get_title() for page in pages]

