# Generated by Django 4.2.1 on 2023-05-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_and_files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Имя файла'),
        ),
    ]