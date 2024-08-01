from django.urls import path
from .views import ProjectsView, ProjectView

urlpatterns = [
    path('', ProjectsView.as_view()),
    path('<slug>', ProjectView.as_view()),
]
