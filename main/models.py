from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """Проекты и их настройки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField('Название мероприятия', max_length=100)  # Название мероприятия
    number_of_participants = models.IntegerField('Количество участников')  # Количество участников
    date = models.DateField('Дата')  # Дата и время
    time = models.TimeField('Время')  # Дата и время
    email = models.CharField('Email', max_length=100)  # Email

    BLEND_MODE_CHOICES = [
        ('1', 'Вариант 1'),
        ('2', 'Вариант 2'),
        ('3', 'Вариант 3'),
        ('4', 'Вариант 4'),
        ('5', 'Вариант 5'),
    ]
    blend_mode = models.CharField('Способ наложения',
                                  max_length=2,
                                  choices=BLEND_MODE_CHOICES,
                                  default='1'
                                  )

    FLY_MODE_CHOICES = [
        ('1', 'Вариант 1'),
        ('2', 'Вариант 2'),
        ('3', 'Вариант 3'),
        ('4', 'Вариант 4'),
        ('5', 'Вариант 5'),
    ]
    fly_mode = models.CharField('Способ слета фото',
                                max_length=2,
                                choices=BLEND_MODE_CHOICES,
                                default='1'
                                )

    final_shot = models.CharField('Финальный кадр', max_length=50)  # Финальный кадр
    # has_central = models.BooleanField('Забронировать места для центральных фото', default=False)

    logo = models.ImageField('Логотип')  # Логотип

    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class Photo(models.Model):
    """Фотографии, загруженные пользователями в определенный альбом для последующего создания фотостены"""
    file = models.ImageField('Файл')
    project_id = models.IntegerField('ID проекта', default=0)  # К какому альбому относится данная фотография
    is_central = models.BooleanField('Центр', default=False)  # Является ли эта фотография центральной
    uploaded_at = models.DateTimeField('Загружено', auto_now_add=True)

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'

