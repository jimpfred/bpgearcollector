# Generated by Django 3.2.4 on 2021-07-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210716_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gear',
            old_name='Description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='gear',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
