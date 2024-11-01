# Generated by Django 5.1.2 on 2024-10-29 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_code', models.IntegerField()),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FunctionalGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification_type', models.CharField(choices=[('Professional', 'Professional'), ('Educational', 'Educational')], max_length=20)),
                ('institution', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('functional_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='HRMS_app.functionalgroup')),
            ],
        ),
        migrations.AddField(
            model_name='functionalgroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='functional_groups', to='HRMS_app.group'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('cnic_no', models.CharField(max_length=13, unique=True)),
                ('husband_or_father_name', models.CharField(max_length=100)),
                ('SAP_ID', models.IntegerField(default=None, unique=True)),
                ('date_of_last_promotion', models.DateField(auto_now=True)),
                ('date_current_posting', models.DateField(auto_now=True)),
                ('date_current_assignment', models.DateField(auto_now=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('phone_no_official', models.CharField(max_length=15)),
                ('phone_no_emergency_contact', models.CharField(max_length=15)),
                ('employee_email', models.EmailField(max_length=100)),
                ('date_of_retirement', models.DateField(blank=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='HRMS_app.branch')),
                ('cadre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.cadre')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='HRMS_app.department')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.designation')),
                ('employee_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.employeegrade')),
                ('employee_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRMS_app.employeetype')),
                ('qualifications', models.ManyToManyField(related_name='employees', to='HRMS_app.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('functional_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='HRMS_app.functionalgroup')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='HRMS_app.region'),
        ),
        migrations.CreateModel(
            name='Wing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wings', to='HRMS_app.division')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='wing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='HRMS_app.wing'),
        ),
    ]
