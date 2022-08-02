from django import forms
from .models import Order


class OrderCreationForm(forms.ModelForm):
    first_name = forms.CharField(error_messages={'required': 'заполните это поле'},
                                 label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    comments = forms.CharField(label='Коментарий', widget=forms.Textarea(
        attrs={'rows': 3, 'class': 'form-control'}
    ), required=False)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'comments']
