from django.urls import path
from . import views


urlpatterns = [
    path('oh_my_box', views.oh_my_box, name="oh_my_box"),
]
