# Generated by Django 3.0 on 2022-05-16 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_title', models.CharField(max_length=128)),
                ('district_description', models.CharField(max_length=255)),
                ('district_status', models.CharField(max_length=100)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.state')),
            ],
        ),
    ]