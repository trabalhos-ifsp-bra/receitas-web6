# Generated by Django 2.2.5 on 2019-09-29 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190929_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='author',
            new_name='autor',
        ),
    ]