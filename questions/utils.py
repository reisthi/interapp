import random

from grade.models import QuestionGrade
from questions.enums import Category
from questions.models import Question


def generate_next_question(session=None):
    """
        Compares answered/not-answered questions and returns a random not answered question to the user.
    """
    answered_ids = list(QuestionGrade.objects
                        .filter(session__pk=session.pk)
                        .values_list('question__pk', flat=True))

    if session.category == Category.GENERAL.value:
        not_answered_ids = list(Question.objects.filter()
                                .exclude(pk__in=answered_ids)
                                .values_list('pk', flat=True))
    else:
        not_answered_ids = list(Question.objects
                                .filter(category=session.category)
                                .exclude(pk__in=answered_ids)
                                .values_list('pk', flat=True))
    if not not_answered_ids:
        return None
    random_question = random.choice(not_answered_ids)
    return Question.objects.filter(pk=random_question).first()


def calculate_scores(session=None):
    return None
