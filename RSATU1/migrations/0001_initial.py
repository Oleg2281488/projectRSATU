# Generated by Django 2.1.3 on 2018-11-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('date', models.DateField(default='10/25/2006')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
