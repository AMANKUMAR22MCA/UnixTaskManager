from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from .utils import simulate_task_lifecycle

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        state = self.request.query_params.get("state")
        if state:
            queryset = queryset.filter(state=state)
        return queryset.order_by("-created_at")

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        simulate_task_lifecycle(task.id)

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
