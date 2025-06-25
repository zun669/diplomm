from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Patient(models.Model):
    GENDER_CHOICES = [
        ('Мужской', 'М'),
        ('Женский', 'Ж')
    ]

    full_name = models.CharField('ФИО', max_length=255)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    contact = models.CharField('Контакты', max_length=255)
    diagnosis = models.TextField('Диагноз')
    recommendations = models.TextField('Рекомендации')
    attending_doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Лечащий врач',
        null=True,
        blank=True
    )

    def get_age(self):
        if not self.birth_date:
            return '?'
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'