from django import forms
from quote_generator.quotes.models import Author
from quote_generator.quotes.models.quote_model import Quote
from quote_generator.quotes.models.choices import ZODIAC_CHOICES, ELEMENT_CHOICES


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = ['added_by']
        labels = {
            'quote': ('Цитат'),
            'author': ('Автор'),
            'sign': ('Зодия'),
            'element': ('Стихия'),
            'image': ('Изображение'),
        }
        
        # widgets = {
        #     'image': forms.FileInput(),
        # }

    def clean(self):
        super(QuoteForm, self).clean()
        quote = self.cleaned_data.get('quote')
        author = self.cleaned_data.get('author')
        sign = self.cleaned_data.get('sign')
        element = self.cleaned_data.get('element')

        if not quote:
            self._errors['quote'] = self.error_class(['Не сте  въвели цитат.'])

        return self.cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': ('Име'),
            'profession': ('Професия'),
            'description': ('Описание'),
            'image': ('Снимка'),
        }



class MyElementForm(forms.Form):
    element = forms.ChoiceField(
        label='Избери стихия',
        widget=forms.Select,
        choices=ELEMENT_CHOICES,
        required=False,
    )
    sign = forms.ChoiceField(
        label='Избери зодия',
        widget=forms.Select,
        choices=ZODIAC_CHOICES,
        required=False,
    )
    moon = forms.ChoiceField(
        label='Избери лунен знак',
        widget=forms.Select,
        choices=ZODIAC_CHOICES,
        required=False,
    )





