from django.urls import path
from .views import newsletterview

urlpatterns = [
    path('', newsletterview.as_view(), name='newsletter'),
]