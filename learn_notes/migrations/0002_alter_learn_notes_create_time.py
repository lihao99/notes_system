# Generated by Django 4.1.4 on 2023-02-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn_notes',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
    ]