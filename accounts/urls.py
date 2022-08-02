from django.urls import path
from .views import login_view, logout_view, register_view, change_profile, password_change, profile
from django.contrib.auth import views


urlpatterns = [
    path('password-reset/done', views.PasswordResetDoneView.as_view(
         template_name='my_password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
         template_name='my_password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete', views.PasswordResetCompleteView.as_view(
         template_name='my_password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-reset', views.PasswordResetView.as_view(
        template_name='my_password_reset_form.html'), name='password_reset'),
    path('password_change', password_change, name='password_change'),
    path('change_profile', change_profile, name='change_profile'),
    path('profile', profile, name='profile'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
