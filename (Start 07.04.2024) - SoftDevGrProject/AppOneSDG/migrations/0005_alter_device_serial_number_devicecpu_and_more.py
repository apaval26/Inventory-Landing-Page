# Generated by Django 4.2.3 on 2024-04-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOneSDG', '0004_alter_equipment_equipaudit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_serial_number',
            name='deviceCPU',
            field=models.CharField(blank=True, max_length=100, verbose_name='Device CPU'),
        ),
        migrations.AlterField(
            model_name='device_serial_number',
            name='deviceGPU',
            field=models.CharField(blank=True, max_length=100, verbose_name='Device GPU'),
        ),
        migrations.AlterField(
            model_name='device_serial_number',
            name='deviceRAM',
            field=models.CharField(blank=True, max_length=100, verbose_name='Device RAM'),
        ),
    ]
