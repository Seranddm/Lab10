# Generated by Django 4.2.1 on 2023-05-05 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('msg_file', models.FileField(blank=True, null=True, upload_to='msg_files/%Y/%m/%d', verbose_name='Файл сообщения')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата отправки')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_messages', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('-send_date',),
            },
        ),
    ]
