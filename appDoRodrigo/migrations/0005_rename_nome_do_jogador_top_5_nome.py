# Generated by Django 3.2.13 on 2023-09-23 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDoRodrigo', '0004_rename_nome_top_5_nome_do_jogador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='top_5',
            old_name='nome_do_jogador',
            new_name='nome',
        ),
    ]
