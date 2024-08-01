from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RealtorWaitlistSerializer
from rest_framework import status

class RealtorWaitlistView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RealtorWaitlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
