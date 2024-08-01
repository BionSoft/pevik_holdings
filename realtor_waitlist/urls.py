from django.urls import path
from .views import RealtorWaitlistView
 
urlpatterns = [
    path('', RealtorWaitlistView.as_view()),
]