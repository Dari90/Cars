# Generated by Django 3.0 on 2020-07-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200718_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='transmission',
            field=models.SmallIntegerField(choices=[(1, 'механика'), (2, 'автомат'), (3, 'робот')], default=0, verbose_name='Transmission'),
        ),
    ]
