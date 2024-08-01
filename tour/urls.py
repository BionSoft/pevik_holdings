from django.urls import path
from .views import ScheduleCreateView

urlpatterns = [
    path('', ScheduleCreateView.as_view()),
]
