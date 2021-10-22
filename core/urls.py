from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('start-session/', views.start_session, name='start'),
    path('categories/<int:session_pk>/', views.choose_category, name='categories'),
    path('session-<int:session_pk>-<int:category>/', views.assign_category, name='session'),
    path('question/<int:session_pk>/', views.show_question, name='show_question'),
    path('report/<int:session_pk>/', views.score, name='report')
]