# Generated by Django 3.2.9 on 2023-06-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='full_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]