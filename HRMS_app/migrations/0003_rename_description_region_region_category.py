# Generated by Django 5.1.2 on 2024-10-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0002_remove_functionalgroup_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='description',
            new_name='region_category',
        ),
    ]