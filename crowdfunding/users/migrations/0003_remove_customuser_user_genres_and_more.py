# Generated by Django 5.1 on 2024-10-25 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
        ('users', '0002_customuser_user_genres_customuser_user_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_genres',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('SU', 'Supporter'), ('BM', 'Band member')], max_length=2),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='users_bands',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.band'),
        ),
    ]