from django.contrib import admin
from django import forms

from .models import Question


# class QuestionModelForm(forms.ModelForm):
#     text = forms.CharField(widget=forms.Textarea)
#     answer = forms.CharField(widget=forms.Textarea)
#     class Meta:
#         model = Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('category', 'difficulty',)
    list_display = ('text', 'category', 'difficulty',)
    # form = QuestionModelForm

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'text': forms.Textarea, 'answer': forms.Textarea}
        return super().get_form(request, obj, **kwargs)
