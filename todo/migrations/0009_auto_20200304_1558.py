# Generated by Django 2.1.5 on 2020-03-04 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20200304_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Project'),
        ),
    ]