# Generated by Django 3.1.7 on 2022-06-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20220625_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]
