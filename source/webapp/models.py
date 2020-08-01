from django.db import models
DEFAULT_STATUS = 'active'
STATUS_CHOICES = [
    (DEFAULT_STATUS, 'Активно'),
    ('blocked', 'Заблокировано'),
]


class Guestbook(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=20, null=False, blank=False, verbose_name='Эл. почта')
    text = models.TextField(max_length=2000, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.name} - {self.text}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
