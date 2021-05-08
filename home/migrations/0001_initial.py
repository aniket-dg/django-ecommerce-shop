# Generated by Django 3.2 on 2021-05-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('isNew', models.BooleanField()),
                ('isInOffer', models.BooleanField()),
                ('discount', models.CharField(max_length=10)),
                ('oldPrice', models.CharField(max_length=20)),
                ('newPrice', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]