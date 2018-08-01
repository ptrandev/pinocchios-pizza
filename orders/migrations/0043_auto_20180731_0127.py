# Generated by Django 2.0.7 on 2018-07-31 01:27

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_auto_20180730_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
