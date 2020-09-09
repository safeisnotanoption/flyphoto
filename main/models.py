from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug


class Project(models.Model):
    """Проекты и их настройки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField('Название мероприятия', max_length=100)  # Название мероприятия
    address = models.CharField('Адрес страницы', max_length=30, unique=True, validators=[validate_slug],
                               help_text='Адрес страницы, на которую будут заходить ваши посетители для загрузки '
                                         'своих фотографий')
    num_of_participants = models.IntegerField('Количество участников',
                                              help_text='Приблизительное количество участников')
    date = models.DateField('Дата')  # Дата
    time = models.TimeField('Время')  # Время
    email = models.EmailField('Email', max_length=100, help_text='Мы вышлем финальное видео на данный email')  # Email
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    checked_out = models.BooleanField('Заказан', default=False)
    checked_at = models.DateTimeField('Когда заказан', auto_now_add=True)

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
    final_shot = models.ImageField('Финальный кадр', default='finals/FlyPhoto.png', upload_to='finals/',
                                   help_text='Изображение, в которое слетаются фотографии')

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'

    def __str__(self):
        return f'{self.project}'


class WebsiteSettings(models.Model):
    """Настройки веб-страницы"""
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    logo = models.ImageField('Логотип', default='logos/FlyPhoto.png', upload_to='logos/',
                             help_text='Логотип, расположенный в заголовке веб-страницы. Допускаются изображения в '
                                       'форматах JPG и PNG, в том числе с прозрачным фоном')  # Логотип
    header_color = models.CharField('Цвет заголовка', default='#FFFFFF', max_length=20,
                                    help_text='Цвет заголовка, на котором будет располагаться логотип')
    background_color = models.CharField('Цвет страницы', default='#FFFFFF', max_length=20,
                                        help_text='Основной цвет страницы')

    class Meta:
        verbose_name = 'веб-страница'
        verbose_name_plural = 'веб-страницы'


class Photo(models.Model):
    """Фотографии, загруженные пользователями в определенный альбом для последующего создания фотостены"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.ImageField('Фотография', upload_to='photos/')
    is_central = models.BooleanField('Центр', default=False)  # Является ли эта фотография центральной
    uploaded_at = models.DateTimeField('Загружено', auto_now_add=True)

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
