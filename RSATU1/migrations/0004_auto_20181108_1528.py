# Generated by Django 2.1.3 on 2018-11-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSATU1', '0003_auto_20181108_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='RSATU1.Tag'),
        ),
    ]
