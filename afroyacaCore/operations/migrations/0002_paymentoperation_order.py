# Generated by Django 2.2.17 on 2021-03-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210322_1218'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentoperation',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
    ]
