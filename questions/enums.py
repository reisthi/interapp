from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.TextChoices):
    GENERAL = 1, _('General')
    PERSONAL = 2, _('Personal')
    TECHNICAL = 3, _('Technical')
    BEHAVIOURAL = 4, _('Behavioural')


class DifficultyLevel(models.TextChoices):
    EASY = 'E', _('Easy')
    MEDIUM = 'M', _('Medium')
    HARD = 'H', _('Hard')


class Grades(models.TextChoices):
    SKIPPED = 'N', _('Not answered')
    POOR = 'P', _('Poor')
    OKAY = 'O', _('Okay')
    GOOD = 'G', _('Good')

