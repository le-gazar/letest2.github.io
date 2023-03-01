from django.urls import path
from .views import home,josue,essai



urlpatterns = [
    path('', home, name='home'),
    path('', josue, name='josue'),
    path('',essai, name="essai"),
]