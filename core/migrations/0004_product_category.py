# Generated by Django 4.2.20 on 2025-04-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
