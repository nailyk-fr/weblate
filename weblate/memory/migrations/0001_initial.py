# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-20 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lang', '0011_auto_20180215_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('target', models.TextField()),
                ('origin', models.TextField()),
                ('source_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory_source', to='lang.Language')),
                ('target_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory_target', to='lang.Language')),
            ],
            options={
                'ordering': ['source'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='memory',
            unique_together=set([('source_language', 'target_language', 'source', 'target', 'origin')]),
        ),
        migrations.AlterIndexTogether(
            name='memory',
            index_together=set([('source_language', 'source')]),
        ),
    ]