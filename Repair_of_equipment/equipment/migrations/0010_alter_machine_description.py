# Generated by Django 4.2 on 2023-05-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0009_machine_description_alter_machine_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]