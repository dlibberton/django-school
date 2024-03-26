# Generated by Django 5.0.3 on 2024-03-26 20:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_app', '0001_initial'),
        ('student_app', '0004_alter_student_good_student_and_more'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='student_app.student'),
        ),
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='a_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='subject_app.subject'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]