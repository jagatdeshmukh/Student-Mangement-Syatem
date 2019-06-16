# Generated by Django 2.2.1 on 2019-06-14 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_parent_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='frist_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='parent',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='app.Department'),
        ),
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='app.Student'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
