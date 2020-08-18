from django.db import models


class Photo(models.Model):
    file = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    album = models.IntegerField()
    is_central = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Project(models.Model):
    number_of_participants = models.IntegerField()
    datetime = models.DateTimeField()
    email = models.CharField(max_length=100)
    has_central = models.BooleanField(default=False)
    blend_mode = models.CharField(max_length=50)
    fly_mode = models.CharField(max_length=50)
    final_shot = models.CharField(max_length=50)
    final_datetime = models.DateTimeField()
    project_name = models.CharField(max_length=100)
    logo = models.ImageField()
    background_image = models.ImageField()
    background_color = models.CharField(max_length=20)
