# Generated by Django 5.1 on 2024-09-17 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='perfil/foto/')),
                ('ocupacao', models.CharField(blank=True, max_length=120)),
                ('descricao', models.TextField(blank=True)),
                ('genero', models.CharField(blank=True, max_length=20)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('cidade', models.CharField(blank=True, max_length=20)),
                ('estado', models.CharField(blank=True, max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfil',
            },
        ),
    ]
