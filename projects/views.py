from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer

# Create your views here.
class ProjectsView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Project.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

class ProjectView(RetrieveAPIView):
    queryset = Project.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'