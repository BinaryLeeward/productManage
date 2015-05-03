# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=512)),
                ('product_type', models.CharField(max_length=256)),
                ('create_time', models.DateTimeField(verbose_name=b'date create')),
                ('img_url', models.CharField(max_length=256)),
            ],
        ),
    ]
