# Generated by Django 3.2.5 on 2021-09-02 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0017_medals_total_meadals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_men',
            name='gold_medal',
            field=models.ForeignKey(blank=True, default='gold', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold_men', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='result_women',
            constraint=models.UniqueConstraint(fields=('gold_medal', 'silver_medal', 'bronze_medal'), name='Unique_winner'),
        ),
    ]
