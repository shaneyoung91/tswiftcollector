# Generated by Django 4.2.3 on 2023-07-27 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tswift',
            name='taylors_version',
        ),
    ]
