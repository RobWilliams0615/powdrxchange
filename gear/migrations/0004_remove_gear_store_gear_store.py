# Generated by Django 4.1.3 on 2022-12-27 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0003_gear_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='store',
        ),
        migrations.AddField(
            model_name='gear',
            name='store',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='store', to='gear.gearplatform'),
            preserve_default=False,
        ),
    ]
