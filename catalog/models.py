from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Inventory(models.Model):
    SPORT_CHOICES = (
        ("Велосипеды", "Велосипеды"),
        ("Самокаты", "Самокаты"),
        ("Горнолыжный спорт", "Горнолыжный спорт"),
        ("Бег", "Бег"),
    )

    name = models.CharField(max_length=100, verbose_name="Название товара", null=True)
    email = models.EmailField(
        default="@gmail.com", verbose_name="Укажите email", blank=True
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите обложку товара", null=True
    )
    about_inv = models.TextField(verbose_name="О товаре", null=True)
    SPORT = models.CharField(
        max_length=20, choices=SPORT_CHOICES, verbose_name="Укажите вид спорта", null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.SPORT}"


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ReviewInv(models.Model):
    reviews_inv = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="reviews_inv"
    )
    text = models.TextField()
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars} - {self.reviews_inv}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
