from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class Posts(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    description = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts',
    )


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()