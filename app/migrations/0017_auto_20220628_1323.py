# Generated by Django 3.2 on 2022-06-28 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_terrain_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpo',
            name='bank_statement_doc',
        ),
        migrations.AlterField(
            model_name='ia',
            name='ia_name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.CreateModel(
            name='BankStatementUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_statement_doc', models.ImageField(upload_to='fpo/bank_statement_documents/')),
                ('fpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fpo')),
            ],
        ),
    ]
