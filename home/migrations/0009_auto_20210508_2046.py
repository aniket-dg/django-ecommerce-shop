# Generated by Django 3.2 on 2021-05-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='newPrice',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='oldPrice',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
