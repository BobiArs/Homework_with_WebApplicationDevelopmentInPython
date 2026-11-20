from django import forms
from django.core.exceptions import ValidationError

class CardForm(forms.Form):
    title = forms.CharField(
        label='Назва картки (Title)',
        min_length=3,
        max_length=50,
        required=True,
        error_messages={
            'required': 'Введіть назву картки — це поле обов’язкове',
            'min_length': 'Назва має містити щонайменше 3 символи',
            'max_length': 'Назва занадто довга (максимум 50 символів)',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть заголовок...'
        })
    )

    description = forms.CharField(
        label='Опис',
        min_length=10,
        max_length=250,
        required=True,
        error_messages={
            'required': 'Додайте короткий опис картки.',
            'min_length': 'Опис занадто короткий (мінімум 10 символів)',
            'max_length': 'Опис перевищує ліміт у 250 символів',
        },
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Введіть опис!'
        })
    )

    image = forms.CharField(
        label='Назва файлу зображення',
        max_length=100,
        required=True,
        error_messages={
            'required': 'Вкажіть назву файлу картинки з папки static/main/images/',
            'max_length': 'Назва файлу занадто довга',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Наприклад: card1.jpg'
        })
    )

    # Кастомна перевірка розширення файлу картинки
    def clean_image(self):
        image = self.cleaned_data.get('image')
        allowed_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        if image and not image.lower().endswith(allowed_extensions):
            raise ValidationError('Файл має закінчуватися на .jpg, .jpeg, .png або .webp!')

        return image