# Generated by Django 2.0.3 on 2018-04-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20180410_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='título da categoria'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(max_length=255, verbose_name='tags'),
        ),
    ]
