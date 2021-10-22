from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'question.html')