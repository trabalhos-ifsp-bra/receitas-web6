# Generated by Django 2.2.5 on 2019-09-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190929_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='receita',
            name='imagem',
            field=models.ImageField(upload_to='receitas'),
        ),
    ]
