# Generated by Django 3.2 on 2021-05-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cart_products_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products_list',
            field=models.JSONField(),
        ),
    ]
