from django.urls import path
from my_first_site.note import views
from my_first_site.dollar import dollar_view


urlpatterns = [
    path('new_model_list', views.New_model_class.as_view(), name='new_model'),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('cart_add_product/<int:product_id>',
         views.cart_add_product, name='cart_add_product'),
    path('cart_remove_all/<int:product_id>',
         views.cart_remove_all, name='cart_remove_all'),
    path('cart_remove/<int:product_id>',
         views.cart_remove, name='cart_remove'),
    path('search/', views.ObjectListView.as_view(), name='search_result'),
    path('product_detail/<int:pk>', views.DetailView.as_view(),
         name='product_detail'),
    path('headphones', views.HeadphonesView.as_view(), name='headphones'),
    path('note', views.NoteView.as_view(), name='note'),
    path('dollar', dollar_view, name='dollar_view'),
    path('', views.index, name='index'),
]
