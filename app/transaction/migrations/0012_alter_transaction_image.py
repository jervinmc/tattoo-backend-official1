# Generated by Django 4.0.1 on 2022-06-16 02:25

from django.db import migrations, models
import transaction.models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_alter_transaction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='image',
            field=models.ImageField(default='uploads/Cases.png', upload_to=transaction.models.nameFile, verbose_name='image'),
        ),
    ]
