# Generated by Django 3.2.13 on 2023-09-23 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDoRodrigo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='top_5',
            old_name='nascimento',
            new_name='nome',
        ),
    ]
