# Generated by Django 2.2.17 on 2021-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20201211_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coretrackedmodel',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='coretrackedmodel',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
