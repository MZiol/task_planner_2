from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Task
from .serializers import TaskSerializer

class TaskFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains') 
    description = filters.CharFilter(field_name='description', lookup_expr='icontains') 
    status = filters.ChoiceFilter(field_name='status', choices=Task.STATUS_CHOICES)
    assigned_user = filters.NumberFilter(field_name='assigned_user')

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'assigned_user']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter