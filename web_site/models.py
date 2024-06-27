from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    article = models.CharField(max_length=255, verbose_name="Статья")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

