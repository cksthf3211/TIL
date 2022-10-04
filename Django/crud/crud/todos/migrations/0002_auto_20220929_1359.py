# Generated by Django 3.2.12 on 2022-09-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]
