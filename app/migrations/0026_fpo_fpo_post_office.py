# Generated by Django 3.2 on 2022-07-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20220707_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpo',
            name='fpo_post_office',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
