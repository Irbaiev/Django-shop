# Generated by Django 4.0.3 on 2022-04-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_grade_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, max_length=12),
        ),
    ]
