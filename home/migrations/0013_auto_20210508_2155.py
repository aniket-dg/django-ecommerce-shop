# Generated by Django 3.2 on 2021-05-08 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_alter_productcart_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='productCart_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]