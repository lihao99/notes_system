# Generated by Django 4.1.4 on 2023-02-10 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('create_time', models.DateTimeField(max_length=16, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department')),
            ],
        ),
    ]
