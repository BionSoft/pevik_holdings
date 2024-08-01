from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScheduleSerializer
from rest_framework import status

class ScheduleCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)