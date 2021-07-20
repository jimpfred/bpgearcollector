# Generated by Django 3.2.4 on 2021-07-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_arrdepdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrdepdate',
            name='type',
            field=models.CharField(choices=[('A', 'Park Arrival'), ('D', 'Park Departure')], default='A', max_length=1),
        ),
    ]