# Generated by Django 5.1.2 on 2024-11-01 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0010_alter_employee_employee_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.employeetype'),
        ),
    ]
