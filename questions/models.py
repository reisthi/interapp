from django.db import models
from .enums import Category, DifficultyLevel


class Question(models.Model):
    text = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    category = models.CharField(max_length=1, choices=Category.choices, default=1, null=False, blank=False)
    difficulty = models.CharField(max_length=1, choices=DifficultyLevel.choices, default=1, null=False, blank=False)

    def __str__(self):
        return f"{self.text}"
