# Generated by Django 4.1.4 on 2023-02-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_notes', '0004_alter_learn_notes_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn_notes',
            name='create_type',
            field=models.IntegerField(choices=[(1, '仅我可见'), (2, '所有人')], default=1, verbose_name='性别'),
        ),
    ]
