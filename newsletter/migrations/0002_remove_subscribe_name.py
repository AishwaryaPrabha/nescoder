# Generated by Django 2.0.8 on 2018-09-21 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='name',
        ),
    ]
