# Generated by Django 3.2.5 on 2021-09-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_auto_20210902_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medals',
            name='bronze_medal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medals',
            name='gold_medal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medals',
            name='silver_medal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]