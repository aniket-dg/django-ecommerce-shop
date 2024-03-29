# Generated by Django 3.2 on 2021-05-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_shoes_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='isInTopSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='category',
            field=models.CharField(choices=[('nike', 'Nike'), ('adidas', 'Adidas'), ('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], max_length=10),
        ),
    ]
