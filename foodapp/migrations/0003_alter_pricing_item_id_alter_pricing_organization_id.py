# Generated by Django 5.0.2 on 2024-02-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_remove_pricing_total_delivery_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='item_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='organization_id',
            field=models.CharField(max_length=200),
        ),
    ]