# Generated by Django 3.1.7 on 2022-06-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.AddField(
            model_name='content',
            name='topic',
            field=models.CharField(default='biologia', max_length=100),
            preserve_default=False,
        ),
    ]
