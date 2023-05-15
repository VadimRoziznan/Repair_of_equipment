# Generated by Django 4.2 on 2023-05-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0008_alter_machine_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
