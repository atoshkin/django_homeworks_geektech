from django import forms
from movies.models import Movie


class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions director'.split()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название!',
                    'rows': 10
                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'director': forms.Select(
                attrs={
                    'class': 'form-control form-control-custom',

                }
            )
        }