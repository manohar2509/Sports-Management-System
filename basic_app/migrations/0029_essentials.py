# Generated by Django 3.2.7 on 2021-11-11 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0028_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shoes', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), (None, 'No allocated')], max_length=10)),
                ('Bag', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), (None, 'No allocated')], max_length=10)),
                ('Jersy', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), (None, 'No allocated')], max_length=10)),
                ('Accomodation', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), (None, 'No allocated')], max_length=10)),
                ('Athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]