# Generated by Django 3.1.2 on 2020-10-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_queue_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='time',
            field=models.DateTimeField(max_length=30),
        ),
    ]
