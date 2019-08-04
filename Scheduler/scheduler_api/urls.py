from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, UpdateView

urlpatterns = {
    url(r'^schedules$', CreateView.as_view(), name="create"),
    url(r'^schedules/(?P<pk>\d+)$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)