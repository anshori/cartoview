# Generated by Django 2.1.3 on 2019-03-11 10:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_remove_layer_refresh_interval'),
        ('app_manager', '0003_auto_20190221_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='No title Provided', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='No Description Provided', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appinstance',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='app_manager.App'),
        ),
        migrations.AddField(
            model_name='appinstance',
            name='layers',
            field=models.ManyToManyField(to='layers.Layer'),
        ),
    ]
