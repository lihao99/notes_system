# Generated by Django 4.1.4 on 2023-02-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_delete_learn_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='账号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
    ]
