# Generated by Django 4.0.3 on 2022-04-16 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_grade_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
