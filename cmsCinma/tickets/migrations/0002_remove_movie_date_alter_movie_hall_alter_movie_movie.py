# Generated by Django 4.2.4 on 2023-09-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.AlterField(
            model_name='movie',
            name='hall',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.CharField(max_length=30),
        ),
    ]
