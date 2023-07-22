# Generated by Django 3.0 on 2022-05-30 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20220530_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='annual_incame',
        ),
        migrations.AddField(
            model_name='farmer',
            name='annual_income',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer',
            name='delete_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('other', 'Other')], max_length=128),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='livestock_income',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='total_capital_amount_deposited',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='fpo',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='fpo',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
    ]
