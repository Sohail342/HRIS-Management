# Generated by Django 5.1.2 on 2024-11-01 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0013_employee_employee_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeetype',
            old_name='type_name',
            new_name='name',
        ),
    ]