from django.db import models


class Slogan(models.Model):
    text = models.CharField(max_length=200, verbose_name="Текс слогана")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоганы"


class TopProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=100, verbose_name="Описание")
    image = models.ImageField(upload_to='images/', verbose_name="Фотокарточка")
    price = models.PositiveIntegerField(default=100, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Популярный продукт"
        verbose_name_plural = "5 популярных продуктов"


class YouTubeVideo(models.Model):
    video_id = models.URLField()

    def __str__(self):
        return self.video_id

    class Meta:
        verbose_name = "Ютуб видео"
        verbose_name_plural = "Ютуб видео"
