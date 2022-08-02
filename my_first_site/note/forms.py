from django import forms
from my_first_site.note.models import Product


class DollarForm(forms.ModelForm):
    rate = forms.DecimalField(label='Курс', max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ('category',)


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'name', 'price')


# class ManufacturerForm(forms.ModelForm):
#     class Meta:
#         model = Manufacturer
#         fields = ('name', 'country')
