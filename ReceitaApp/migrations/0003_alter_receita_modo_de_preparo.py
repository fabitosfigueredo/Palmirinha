# Generated by Django 4.2.7 on 2023-11-09 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0002_receita_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='modo_de_preparo',
            field=models.TextField(max_length=8001),
        ),
    ]