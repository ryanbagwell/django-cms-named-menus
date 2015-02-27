# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_named_menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cmsnamedmenu',
            options={'verbose_name': 'CMS Menu', 'verbose_name_plural': 'CMS Menus'},
        ),
    ]
