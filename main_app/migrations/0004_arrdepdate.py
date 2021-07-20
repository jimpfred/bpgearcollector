# Generated by Django 3.2.4 on 2021-07-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210716_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrDepDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.hiker')),
            ],
        ),
    ]