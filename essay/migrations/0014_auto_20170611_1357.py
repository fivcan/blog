# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '00013_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='essay',
            new_name='EssayInfo',
        ),
    ]
