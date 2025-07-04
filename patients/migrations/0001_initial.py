# Generated by Django 5.2.3 on 2025-06-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('diagnosis', models.TextField(verbose_name='Диагноз')),
                ('recommendations', models.TextField(verbose_name='Рекомендации')),
            ],
        ),
    ]
