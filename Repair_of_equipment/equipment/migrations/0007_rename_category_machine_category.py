# Generated by Django 4.2 on 2023-05-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_remove_category_machine_generaltable_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='Category',
            new_name='category',
        ),
    ]
