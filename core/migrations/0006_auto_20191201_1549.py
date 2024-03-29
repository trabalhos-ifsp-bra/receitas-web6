# Generated by Django 2.2.5 on 2019-12-01 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_categoria_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='rating',
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Receita')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
