# Generated by Django 2.0.2 on 2018-02-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protected_links', '0006_auto_20180206_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='user_agent',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='links',
            name='user_agent',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
