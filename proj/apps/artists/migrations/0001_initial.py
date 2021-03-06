# Generated by Django 3.2.1 on 2021-05-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='نام هنرمند')),
                ('last_name', models.CharField(blank=True, max_length=225, null=True, verbose_name='نام خانوادگی هنرمند')),
                ('alias', models.CharField(max_length=225, verbose_name='نام')),
            ],
            options={
                'verbose_name_plural': 'هنرمندان',
            },
        ),
    ]
