# Generated by Django 2.2.17 on 2021-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='size',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='variety',
            name='is_published',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]