from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LoginView, RegistrationView


urlpatterns = [
    path('login', LoginView.as_view(), name="signin"),
    path('registration', RegistrationView.as_view(), name="registration"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
