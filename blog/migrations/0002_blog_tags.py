# Generated by Django 4.0.3 on 2022-04-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(choices=[('all', 'all'), ('technology', 'Technology'), ('food', 'Food'), ('fashion', 'Fashion')], default='all', max_length=20),
        ),
    ]
