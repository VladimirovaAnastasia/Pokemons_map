# Generated by Django 2.2.3 on 2019-10-17 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolution_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pokemon_entities.Pokemon', verbose_name='Эволюционирует от'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок EN'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок JP'),
        ),
    ]
