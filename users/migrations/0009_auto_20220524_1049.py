# Generated by Django 3.0 on 2022-05-24 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='status',
            new_name='delete_status',
        ),
    ]