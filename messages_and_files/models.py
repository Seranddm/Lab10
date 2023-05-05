from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        to=User,
        verbose_name='Отправитель',
        related_name='send_messages',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        to=User, verbose_name='Получатель',
        related_name='receive_messages',
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name='Текст сообщения')
    msg_file = models.FileField(verbose_name='Файл сообщения', upload_to='msg_files/%Y/%m/%d', blank=True, null=True)
    file_name = models.CharField(verbose_name='Имя файла', max_length=100, blank=True)
    send_date = models.DateTimeField(verbose_name='Время и дата отправки', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'  # Имя модели в единственном числе
        verbose_name_plural = 'Сообщения'  # Имя модели во множественном числе
        ordering = ('-send_date',)
