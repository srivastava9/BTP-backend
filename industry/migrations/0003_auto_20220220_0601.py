# Generated by Django 3.2.7 on 2022-02-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_auto_20220220_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventories'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image of Employee'),
        ),
    ]
