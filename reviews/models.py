import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() 

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_author", verbose_name='Автор')
    review_date = models.DateField(default=datetime.date.today, verbose_name='Дата публикации')
    job_status = models.BooleanField(default=False, verbose_name='Нашел работу')
    reply = models.IntegerField(default=0, verbose_name='Откликов')
    replies_from_employer = models.IntegerField(default=0, verbose_name='Собеседований')
    test_tasks = models.IntegerField(default=0, verbose_name='Тестовых')
    offers = models.IntegerField(default=0, verbose_name='Офферов')
    comment = models.TextField(default='', verbose_name='Коммент')

    class Meta:
        ordering = ['-review_date']
