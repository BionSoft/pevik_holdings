from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import OrderingFilter
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, listingDetailSerializer
from datetime import datetime, timezone, timedelta

class ListingsView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    filter_backends = [OrderingFilter] 
    ordering_fields = ['price', 'list_date']  
    ordering = ['-list_date']
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = listingDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        queryset = Listing.objects.filter(is_published=True)
        data = request.data

        # Category filter
        category = data.get('category', '')
        if category:
            queryset = queryset.filter(property_type__iexact=category)

        # Sale type filter
        sale_type = data.get('sale_type', '')
        if sale_type:
            queryset = queryset.filter(sale_type__iexact=sale_type)

        # Minimum price filter
        min_price = data.get('min_price', '')
        if min_price:
            try:
                min_price = int(min_price)
                queryset = queryset.filter(price__gte=min_price)
            except ValueError:
                return Response({"error": "Invalid value for min_price. Please provide a valid integer."}, status=400)

        # Bedrooms filter
        bedrooms = data.get('bedrooms', '')
        if bedrooms:
            try:
                bedrooms = int(bedrooms)
                queryset = queryset.filter(bedrooms__gte=bedrooms)
            except ValueError:
                return Response({"error": "Invalid value for bedrooms. Please provide a valid integer."}, status=400)

        # Bathrooms filter
        bathrooms = data.get('bathrooms', '')
        if bathrooms:
            try:
                bathrooms = float(bathrooms)
                queryset = queryset.filter(bathrooms__gte=bathrooms)
            except ValueError:
                return Response({"error": "Invalid value for bathrooms. Please provide a valid number."}, status=400)

        # Keywords filter
        keywords = data.get('keywords', '')
        if keywords:
            queryset = queryset.filter(description__icontains=keywords)

        # Days listed filter
        days_listed = data.get('days_listed', '')
        if days_listed:
            try:
                days_listed = int(days_listed)
                cutoff_date = datetime.now() - timedelta(days=days_listed)
                queryset = queryset.filter(list_date__gte=cutoff_date)
            except ValueError:
                return Response({"error": "Invalid value for days_listed. Please provide a valid integer."}, status=400)

        # Number of photos filter
        min_photos = data.get('min_photos', '')
        if min_photos:
            try:
                min_photos = int(min_photos)
                queryset = [
                    listing for listing in queryset 
                    if sum(1 for photo in [
                        listing.photo_main, listing.photo_1, listing.photo_2, 
                        listing.photo_3, listing.photo_4, listing.photo_5, 
                        listing.photo_6, listing.photo_7, listing.photo_8, 
                        listing.photo_9, listing.photo_10, listing.photo_11, 
                        listing.photo_12, listing.photo_13, listing.photo_14, listing.photo_15] 
                        if photo) >= min_photos
                ]
            except ValueError:
                return Response({"error": "Invalid value for min_photos. Please provide a valid integer."}, status=400)

        serializer = ListingSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class BasicSearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        data = request.data

        property_type = data.get('property_type', '')
        days_passed = data.get('days_listed', 'Any')

        queryset = Listing.objects.filter(is_published=True, property_type__iexact=property_type)

        if days_passed != 'Any':
            try: 
                days_passed = int(days_passed)
                if days_passed <= 0:
                    raise ValueError("Invalid value for days_passed")
                cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_passed)
                queryset = queryset.filter(list_date__gte=cutoff_date)
            except ValueError:
                # Handle invalid integer input for days_passed
                return Response({"error": "Invalid value for days_listed. Please provide a positive integer."}, status=400)

        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)

class PropertyTypePageView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer

    def get(self, request, property_type, format=None):
        # Fetch listings for the specified property type
        queryset = Listing.objects.filter(property_type__iexact=property_type)
        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)