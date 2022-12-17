from .models import Test
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class TestForm(ModelForm):
    class Meta:
        model = Test

        fields = ['title', 'anons', 'ans1', 'pr1', 'ans2', 'pr2', 'ans3', 'pr3']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вопроса'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            'ans1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 1'
            }),
            'pr1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 2'
            }),
            'pr2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 3'
            }),
            'pr3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            })
        }

class Testans(ModelForm):
    class Meta:
        model = Test

        fields = ['title', 'anons', 'ans1', 'pr1', 'ans2', 'pr2', 'ans3', 'pr3']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вопроса'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            'ans1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 1'
            }),
            'pr1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 2'
            }),
            'pr2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 3'
            }),
            'pr3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            })
        }