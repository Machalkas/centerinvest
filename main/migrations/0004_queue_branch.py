# Generated by Django 3.1.2 on 2020-10-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201010_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='branch',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.branch'),
        ),
    ]
