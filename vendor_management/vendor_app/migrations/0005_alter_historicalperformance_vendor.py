# Generated by Django 4.2.7 on 2023-11-29 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0004_historicalperformance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_performances', to='vendor_app.vendor'),
        ),
    ]
