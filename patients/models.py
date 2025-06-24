from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    GENDER_CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    ]

    full_name = models.CharField('ФИО', max_length=255)
    contact = models.CharField('Контакты', max_length=255)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)  # Добавлено
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    diagnosis = models.TextField('Диагноз')
    recommendations = models.TextField('Рекомендации')
    attending_doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Лечащий врач',
    )

    def get_age(self):
        from datetime import date
        if not self.birth_date:
            return '?'
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'