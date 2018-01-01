# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import article.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=article.models.new_file_name, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
