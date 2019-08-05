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
        fields = ('id', 'job_name', 'command', 'schedule_time', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


    def create(self, validated_data):
        """Creates record of the schedule and stores in the backend along with adding , """
        """the relevant job to the apscheduler queue."""
        schedule = Schedule.objects.create(**validated_data)
        command = validated_data.pop('command')
        schedule_time = validated_data.pop('schedule_time')

        self.add_job_to_scheduler(command, schedule.id, schedule_time)
        return schedule

    def add_job_to_scheduler(self, command, id, schedule_time):
        """Add job to the scheduler."""
        def _add_schedule():
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print output
        
        scheduler.add_job(_add_schedule, 'date', run_date=schedule_time, id=str(id))
        print scheduler.print_jobs()
