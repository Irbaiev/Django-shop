# Generated by Django 3.2.8 on 2022-07-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./image', verbose_name='image'),
        ),
    ]
