# Generated by Django 2.2.1 on 2019-06-11 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190607_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendence',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_attendence', to='app.Student'),
        ),
    ]
