# Generated by Django 3.1.7 on 2022-06-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20220625_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
