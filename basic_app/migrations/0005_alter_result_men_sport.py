# Generated by Django 3.2.5 on 2021-09-02 07:17

import basic_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20210902_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_men',
            name='sport',
            field=models.CharField(blank='False', choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=32,),
        ),
    ]