# Generated by Django 5.1 on 2024-08-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_category_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
