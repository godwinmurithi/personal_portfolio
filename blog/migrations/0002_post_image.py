# Generated by Django 4.1.3 on 2022-11-21 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FilePathField(default=django.utils.timezone.now, verbose_name='/img/00.jpeg'),
            preserve_default=False,
        ),
    ]
