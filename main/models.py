from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import validate_slug


class Project(models.Model):
    """Проекты и их настройки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField('Название мероприятия', max_length=100)  # Название мероприятия
    address = models.CharField('Адрес страницы', max_length=30, unique=True, validators=[validate_slug])
    num_of_participants = models.IntegerField('Количество участников')  # Количество участников
    date = models.DateField('Дата')  # Дата
    time = models.TimeField('Время')  # Время
    email = models.CharField('Email', max_length=100)  # Email
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self):  # new
        return f'{self.address} ({self.user})'

    # def get_absolute_url(self):  # new
    #     return reverse('university_detail', args=[str(self.id)])


class VideoSettings(models.Model):
    """Настройки видео"""
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    # Способ наложения
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
    # Способ слета фото
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
    # Финальный кадр
    final_shot = models.CharField('Финальный кадр', max_length=50, default='Финальный кадр')  # Финальный кадр

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'

    def __str__(self):
        return f'{self.project}'


class WebsiteSettings(models.Model):
    """Настройки веб-страницы"""
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    logo = models.ImageField('Логотип')  # Логотип
    header_color = models.CharField('Цвет заголовка', max_length=20)
    background_color = models.CharField('Цвет страницы', max_length=20)

    class Meta:
        verbose_name = 'веб-страница'
        verbose_name_plural = 'веб-страницы'


class Photo(models.Model):
    """Фотографии, загруженные пользователями в определенный альбом для последующего создания фотостены"""
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    file = models.ImageField('Файл')
    is_central = models.BooleanField('Центр', default=False)  # Является ли эта фотография центральной
    uploaded_at = models.DateTimeField('Загружено', auto_now_add=True)

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
