from datetime import datetime
from django.db import models

from questions.enums import Category


class Session(models.Model):
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=20, blank=False, null=False, unique=True)
    number_of_questions = models.IntegerField(blank=False, null=True)
    category = models.CharField(max_length=1, choices=Category.choices, default='G', null=True, blank=True)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk}"

