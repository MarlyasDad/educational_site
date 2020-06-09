from datetime import datetime
from django.contrib import auth
from django import forms
from .models import Feedback


class MyBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control form-control-{field_name} w-100'
            # field.help_text = ''
            # if field_name == 'password':
            #     field.widget = forms.HiddenInput()


class FeedbackForm(MyBaseForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ['author', 'create']
