# Generated by Django 2.0.7 on 2018-08-01 04:58

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0050_item_extras_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='extras_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
