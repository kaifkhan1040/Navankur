# Generated by Django 3.2 on 2022-06-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20220620_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cbbo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbbo_name', models.CharField(max_length=128)),
            ],
        ),
    ]
