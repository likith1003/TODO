# Generated by Django 4.1.7 on 2023-06-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False, verbose_name='Sno')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('desc', models.TextField(verbose_name='Desc')),
            ],
        ),
    ]
