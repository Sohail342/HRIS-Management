# Generated by Django 5.1.2 on 2024-10-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRMS_app', '0005_branch_branch_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
