# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.TextField()),
            ],
        ),
    ]
