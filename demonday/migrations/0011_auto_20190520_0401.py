# Generated by Django 2.2.1 on 2019-05-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demonday', '0010_auto_20190520_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='dispHora',
            new_name='fimHora',
        ),
        migrations.AddField(
            model_name='perfil',
            name='iniHora',
            field=models.TimeField(blank=True, default=''),
        ),
    ]