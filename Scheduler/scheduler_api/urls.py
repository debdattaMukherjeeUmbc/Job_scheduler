from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateListView

urlpatterns = {
    url(r'^schedules$', CreateListView.as_view(), name="list_create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)