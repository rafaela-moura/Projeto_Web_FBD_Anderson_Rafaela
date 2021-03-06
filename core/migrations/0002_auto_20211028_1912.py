# Generated by Django 3.2.7 on 2021-10-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='filmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('genero', models.CharField(choices=[('TERROR', 'Terror'), ('ACAO', 'Ação'), ('ROMANCE', 'Romance'), ('COMEDIA', 'Comédia'), ('AVENTURA', 'Aventura'), ('DRAMA', 'Drama'), ('SUSPENCE', 'Suspense')], max_length=20, verbose_name='Gênero')),
                ('tempo_duracao', models.CharField(max_length=10, verbose_name='Tempo de Duração')),
                ('idioma', models.CharField(choices=[('DUB', 'Dublado'), ('LEG', 'Legendado')], max_length=20, verbose_name='Idioma')),
            ],
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
