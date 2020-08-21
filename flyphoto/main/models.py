from django.db import models


class Photo(models.Model):
    """Фотографии, загруженные пользователями в определенный альбом для последующего создания фотостены"""
    file = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    album = models.IntegerField(default=0)  # К какому альбому относится данная фотография
    is_central = models.BooleanField(default=False)  # Является ли эта фотография центральной

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'


class Project(models.Model):
    """Проекты и их настройки"""
    project_name = models.CharField(max_length=100)  # Название мероприятия
    number_of_participants = models.IntegerField()  # Количество участников
    datetime = models.DateTimeField()  # Дата и время
    email = models.CharField(max_length=100)  # Email

    blend_mode = models.CharField(max_length=50)  # Способ наложения
    fly_mode = models.CharField(max_length=50)  # Способ слета фото
    final_shot = models.CharField(max_length=50)  # Финальный кадр
    has_central = models.BooleanField(default=False)  # Забронировать центральные места

    logo = models.ImageField()  # Логотип
    background_color = models.CharField(max_length=20)  # Цвет фона

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
