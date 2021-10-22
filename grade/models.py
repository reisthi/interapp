from django.db import models

from core.models import Session
from questions.enums import Grades
from questions.models import Question


class QuestionGrade(models.Model):
    session = models.ForeignKey(Session, null=False, blank=False, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.PROTECT)
    grade = models.CharField(max_length=1, choices=Grades.choices, default=0, null=False, blank=False)
