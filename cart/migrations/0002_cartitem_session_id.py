# Generated by Django 4.2.6 on 2023-10-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='session_id',
            field=models.CharField(default='', max_length=32),
        ),
    ]
