# Generated by Django 2.2 on 2019-05-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='layer URL'),
        ),
    ]
