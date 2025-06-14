# Generated by Django 5.0.2 on 2024-04-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCoefficient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km_price_coefficient', models.FloatField(default=1.4)),
                ('flat_rate_coefficient', models.FloatField(default=2)),
            ],
        ),
    ]
