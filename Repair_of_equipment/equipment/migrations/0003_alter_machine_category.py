# Generated by Django 4.2 on 2023-05-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_machine_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
