# Generated by Django 4.2.2 on 2023-06-29 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_customusuario_vencimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='vencimento',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
