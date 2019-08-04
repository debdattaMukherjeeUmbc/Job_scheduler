from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import pagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from .serializers import ScheduleSerializer
from .models import Schedule

class ResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # import pdb;pdb.set_trace()
    queryset = Schedule.objects.all()
    pagination_class = ResultsSetPagination
    serializer_class = ScheduleSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
    	# import pdb;pdb.set_trace()
        return self.create(request)

    def perform_create(self, serializer):
    	# import pdb;pdb.set_trace()
        serializer.save()
        


class UpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

