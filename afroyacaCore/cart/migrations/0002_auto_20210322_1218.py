# Generated by Django 2.2.17 on 2021-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]