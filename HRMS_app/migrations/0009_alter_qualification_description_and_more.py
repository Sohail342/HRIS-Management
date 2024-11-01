# Generated by Django 5.1.2 on 2024-10-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0008_alter_division_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='institution',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='qualification_type',
            field=models.CharField(blank=True, choices=[('Professional', 'Professional'), ('Educational', 'Educational')], default=None, max_length=20, null=True),
        ),
    ]
