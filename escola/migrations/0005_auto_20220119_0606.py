# Generated by Django 3.1.3 on 2022-01-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_aluno_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='capa',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=10),
        ),
    ]