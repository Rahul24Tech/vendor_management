# Generated by Django 4.2.7 on 2023-11-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0003_remove_historicalperformance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]