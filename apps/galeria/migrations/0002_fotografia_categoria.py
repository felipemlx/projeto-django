# Generated by Django 4.2.1 on 2023-05-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('BAIXO', 'Baixo'), ('GUITARRA', 'Guitarra')], default='', max_length=100),
        ),
    ]
