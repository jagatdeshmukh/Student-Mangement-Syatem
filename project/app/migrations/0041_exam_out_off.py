# Generated by Django 2.2.1 on 2019-06-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20190614_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='out_off',
            field=models.IntegerField(default=100),
        ),
    ]
