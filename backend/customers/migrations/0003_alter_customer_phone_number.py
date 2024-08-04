# Generated by Django 5.0.7 on 2024-08-03 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
    ]