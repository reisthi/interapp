from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse

from grade.models import QuestionGrade
from questions.enums import Category
from questions.utils import generate_next_question, calculate_scores
from .forms import StartSessionForm, QuestionGradeForm
from .models import Session


def index(request):
    return TemplateResponse(request, 'index.html')


def start_session(request):
    """ Checks if book is not being ordered by anyone before deletes it. """
    form = StartSessionForm(request.POST or None)
    if form.is_valid():
        session = form.save()
        session.save()
        return redirect('core:categories', session.pk)
    context = {'form': form}
    return TemplateResponse(request, 'session_form.html', context)


def choose_category(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    context = {'session_pk': session.pk, 'categories': Category.__members__}
    return TemplateResponse(request, 'category.html', context)


def assign_category(request, session_pk, category):
    session = get_object_or_404(Session, pk=session_pk)
    session.category = category
    session.save()
    return show_question(request, session_pk)


def show_question(request, session_pk=None):
    session = get_object_or_404(Session, pk=session_pk)
    next_question = generate_next_question(session)

    if not next_question:
        return redirect('core:report', session.pk)

    form = QuestionGradeForm(request.POST or None, initial={
        'session': session,
        'question': next_question,
    })
    if form.is_valid():
        grade = QuestionGrade()
        grade.session = session
        grade.question = form.cleaned_data['question']
        grade.grade = form.cleaned_data['grade']
        grade.save()
        return redirect('core:show_question', session.pk)
    context = {'form': form, 'question': next_question, 'session': session}
    return TemplateResponse(request, 'question_form.html', context)


def score(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    grades = QuestionGrade.objects.filter(session=session)
    context = {'report': grades, 'session': session}
    return TemplateResponse(request, 'report.html', context)