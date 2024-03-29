# Generated by Django 5.0.2 on 2024-02-24 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the food Item', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.CharField(help_text='Enter the organization ID.', max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the organization name.', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill_Per_Item',
            fields=[
                ('bill_id_per_item', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('date_of_purchase', models.DateField(blank=True, null=True)),
                ('quantity', models.CharField(max_length=100)),
                ('bill_amt', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='foodapp.item')),
                ('organization_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='foodapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('pricing_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('zone', models.CharField(max_length=200)),
                ('base_distance_in_km', models.CharField(max_length=200)),
                ('item_price_per_pack', models.CharField(max_length=200)),
                ('km_price', models.FloatField()),
                ('fix_price', models.FloatField()),
                ('total_delivery_price', models.FloatField()),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='foodapp.item')),
                ('organization_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='foodapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='TotalBill',
            fields=[
                ('bill_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('date_of_purchase', models.DateField(blank=True, null=True)),
                ('total_bill_amt', models.CharField(max_length=100)),
                ('bill_id_per_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='foodapp.bill_per_item')),
            ],
        ),
    ]
