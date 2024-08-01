from django.urls import path
from .views import ListingsView, ListingView, SearchView, BasicSearchView, PropertyTypePageView

urlpatterns = [
    path('', ListingsView.as_view()),
    path('search', SearchView.as_view()),
    path('basicsearch', BasicSearchView.as_view()),
    path('property-type/<str:property_type>/', PropertyTypePageView.as_view()),
    path('<slug>', ListingView.as_view()),
]
