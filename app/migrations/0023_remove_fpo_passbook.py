# Generated by Django 3.2 on 2022-07-07 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20220707_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpo',
            name='Passbook',
        ),
    ]