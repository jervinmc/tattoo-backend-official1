# Generated by Django 4.0.1 on 2022-04-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='category_name')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]