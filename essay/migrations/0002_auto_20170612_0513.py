# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='message',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='user',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
