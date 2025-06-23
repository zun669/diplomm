from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    birth_date = models.DateField("Дата рождения")
    diagnosis = models.TextField("Диагноз")
    recommendations = models.TextField("Рекомендации")

    def __str__(self):
        return self.full_name