# Generated by Django 5.0.1 on 2024-01-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coroa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('código', models.CharField(max_length=255)),
                ('número', models.CharField(max_length=255)),
                ('colo_superior', models.CharField(max_length=255)),
                ('colo_inferior', models.CharField(max_length=255)),
                ('furo_anel', models.CharField(max_length=255)),
                ('folga_anel', models.CharField(max_length=255)),
                ('encaixe_co_bl', models.CharField(max_length=255)),
                ('externo', models.CharField(max_length=255)),
                ('situacao_final', models.CharField(max_length=255)),
            ],
        ),
    ]