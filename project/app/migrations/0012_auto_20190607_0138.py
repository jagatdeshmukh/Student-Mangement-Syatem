# Generated by Django 2.2.1 on 2019-06-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190607_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(related_name='_student_subject_+', to='app.Subject'),
        ),
    ]
