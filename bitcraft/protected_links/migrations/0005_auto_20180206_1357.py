# Generated by Django 2.0.2 on 2018-02-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protected_links', '0004_auto_20180206_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='links',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
