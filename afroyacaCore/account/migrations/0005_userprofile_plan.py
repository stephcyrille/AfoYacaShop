# Generated by Django 2.2.17 on 2021-03-27 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybox', '0004_remove_boxsubscriptionplan_subscriber'),
        ('account', '0004_auto_20210322_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mybox.BoxSubscriptionPlan'),
        ),
    ]
