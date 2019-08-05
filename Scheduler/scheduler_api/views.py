from rest_framework import generics
from rest_framework import pagination
from .serializers import ScheduleSerializer
from .models import Schedule

class ResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10


class CreateListView(generics.ListCreateAPIView):
    """This class helps create and list schedules."""
    queryset = Schedule.objects.all()
    pagination_class = ResultsSetPagination
    serializer_class = ScheduleSerializer

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save()
        

