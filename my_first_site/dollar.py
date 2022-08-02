
from django.shortcuts import render, redirect
from my_first_site.note.models import Product
from my_first_site.note.forms import DollarForm


def get_all_items(request):
    product_obj = Product.objects.all()
    note = Product.objects.filter(category='notebook')
    monitor = Product.objects.filter(category='monitor')
    context = {
        'product_obj': product_obj,
        'note': note,
        'monitor': monitor,
    }
    return context


def dollar_view(request):
    form = DollarForm()
    if request.method == "POST":
        form = DollarForm(request.POST)
        if form.is_valid():
            form_category = form.cleaned_data['category']
            number = form.cleaned_data.get('rate')
            # фильтруем товары по конкретной категории
            prod_category = Product.objects.filter(category=form_category)
            for p in prod_category:
                new_price = p.price * number
                p.price = new_price
                p.save()
                context = {'form': form, 'all': get_all_items(request)}
            return render(request, 'dollar_form.html', context)
    else:
        form = DollarForm()
        context = {'form': form, 'all': get_all_items(request)}
        return render(request, 'dollar_form.html', context)
