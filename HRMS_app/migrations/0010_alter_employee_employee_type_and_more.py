# Generated by Django 5.1.2 on 2024-11-01 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0009_alter_qualification_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.employeetype', to_field='type_name'),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='type_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='qualification_type',
            field=models.CharField(blank=True, choices=[('Professional', 'Professional'), ('Educational', 'Educational')], default='Educational', max_length=20, null=True),
        ),
    ]