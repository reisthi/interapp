from django import forms

from grade.models import QuestionGrade
from .models import Session


class StartSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['username']
        widgets = {
            # 'username': forms.HiddenInput(),
            # 'username': forms.TextInput(
            #     attrs={'placeholder': 'Enter description here'}),
        }
        placeholder = {
            'username': 'Some useful help text.'
        }
        error_messages = {
            'username': {
                'required': "Username is required.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['autocomplete'] = 'off'
                field.widget.attrs['required'] = 'required'


class QuestionGradeForm(forms.ModelForm):

    class Meta:
        model = QuestionGrade
        fields = ['question', 'session', 'grade']
        widgets = {
            'session': forms.HiddenInput(),
            'question': forms.HiddenInput(),
            # 'username': forms.TextInput(
            #     attrs={'placeholder': 'Enter description here'}),
        }
        # placeholder = {
        #     'username': 'Some useful help text.'
        # }
        # error_messages = {
        #     'username': {
        #         'required': "Username is required.",
        #     },
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            # field.widget.attrs['required'] = 'required'
