# Generated by Django 2.1.3 on 2018-11-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSATU1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default='10/25/2000'),
        ),
    ]
