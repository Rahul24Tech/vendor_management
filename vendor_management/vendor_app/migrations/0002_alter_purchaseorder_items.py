# Generated by Django 4.2.7 on 2023-11-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.CharField(max_length=250),
        ),
    ]
