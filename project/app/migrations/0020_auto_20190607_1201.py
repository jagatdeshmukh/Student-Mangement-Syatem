# Generated by Django 2.2.1 on 2019-06-07 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20190607_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='app.Course'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='app.Subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject_name',
            field=models.ManyToManyField(related_name='student', to='app.Subject'),
        ),
        migrations.AlterField(
            model_name='student_attendence',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_attendence', to=settings.AUTH_USER_MODEL),
        ),
    ]
