# Generated by Django 4.0.1 on 2022-06-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_transaction_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='estimated_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='estimated_time'),
        ),
    ]
