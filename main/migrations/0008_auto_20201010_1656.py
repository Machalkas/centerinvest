# Generated by Django 3.1.2 on 2020-10-10 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201010_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Номер в очереди'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.branch', verbose_name='Фелиал'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services', verbose_name='Услуга'),
        ),
    ]
