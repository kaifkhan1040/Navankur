# Generated by Django 3.2 on 2022-07-26 07:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_authorisedsharedcapital'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedSharedCapital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('no_of_share', models.CharField(max_length=5)),
                ('face_value', models.CharField(max_length=10)),
                ('total_value', models.CharField(max_length=15)),
                ('fpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fpo')),
            ],
        ),
    ]
