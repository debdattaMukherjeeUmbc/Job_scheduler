from django.core.management import call_command
import datetime
from rest_framework import serializers
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
from pytz import utc

from apscheduler.schedulers.base import STATE_RUNNING 

from .models import Schedule
from updater import scheduler


class ScheduleSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Schedule
        fields = ('id', 'job_name', 'job_description','command', 'start_time', 'end_time', 'job_frequency', 'duration', 'is_active', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        command = validated_data.pop('command')
        start_time = validated_data.pop('start_time')
        schedule = Schedule.objects.create(**validated_data)
        self.add_job_to_scheduler(command, schedule.id, start_time)
        return schedule

    def add_job_to_scheduler(self, command, id, start_time):
        def _add_bash():
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print output
        
        trigger_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
        scheduler.add_job(_add_bash, 'date', run_date=start_time, id=str(id))
        print scheduler.print_jobs()
