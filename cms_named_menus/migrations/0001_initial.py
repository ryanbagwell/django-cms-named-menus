# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMSNamedMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('pages', jsonfield.fields.JSONField(default=[], null=True, blank=True)),
            ],
            options={
                'verbose_name': 'CMS Named Menu',
                'verbose_name_plural': 'CMS Named Menus',
            },
            bases=(models.Model,),
        ),
    ]
