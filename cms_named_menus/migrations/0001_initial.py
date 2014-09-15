# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CMSNamedMenu'
        db.create_table(u'cms_named_menus_cmsnamedmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('pages', self.gf('jsonfield.fields.JSONField')(default=[], null=True, blank=True)),
        ))
        db.send_create_signal(u'cms_named_menus', ['CMSNamedMenu'])


    def backwards(self, orm):
        # Deleting model 'CMSNamedMenu'
        db.delete_table(u'cms_named_menus_cmsnamedmenu')


    models = {
        u'cms_named_menus.cmsnamedmenu': {
            'Meta': {'object_name': 'CMSNamedMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pages': ('jsonfield.fields.JSONField', [], {'default': '[]', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        }
    }

    complete_apps = ['cms_named_menus']