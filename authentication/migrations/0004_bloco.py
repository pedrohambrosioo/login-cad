# Generated by Django 5.0.1 on 2024-01-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_forma_delete_tabelateste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('código', models.CharField(max_length=255)),
                ('número', models.CharField(max_length=255)),
                ('colo', models.CharField(max_length=255)),
                ('rodape', models.CharField(max_length=255)),
                ('flexa', models.CharField(max_length=255)),
                ('furo_de_escape', models.CharField(max_length=255)),
                ('encaixe_ffo', models.CharField(max_length=255)),
                ('externo', models.CharField(max_length=255)),
                ('situacao_final', models.CharField(max_length=255)),
            ],
        ),
    ]
