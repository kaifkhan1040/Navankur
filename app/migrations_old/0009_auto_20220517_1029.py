# Generated by Django 3.0 on 2022-05-17 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220517_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='district',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.AddField(
            model_name='city',
            name='districtid',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
    ]
