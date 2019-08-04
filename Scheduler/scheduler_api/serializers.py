from django.core.management import call_command
from rest_framework import serializers
import subprocess
from subprocess import Popen, PIPE, STDOUT
from .models import Schedule
# from apscheduler.schedulers.background import BackgroundScheduler

from pytz import utc
import datetime
import time
# from apscheduler.schedulers.background import BackgroundScheduler
from . import updater

from pytz import utc
from django.db import transaction
from updater import scheduler

# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor



class ScheduleSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Schedule
        fields = ('id', 'job_name', 'job_description','command', 'start_time', 'end_time', 'job_frequency', 'duration', 'is_active', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    @transaction.atomic
    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        command = validated_data.pop('command')
        # print 'creating.....'
        schedule = Schedule.objects.create(**validated_data)
        jobstores = {
            'mongo': {'type': 'mongodb'},
            'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        executors = {
            'default': {'type': 'threadpool', 'max_workers': 20},
            'processpool': ProcessPoolExecutor(max_workers=5)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }
        scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
        def add_processing_job():
            def _trigger_command():
                print '_trigger_command.....'
                f= open("/Users/dm029579/.virtualenvs/SAP/my_files/yayyy.txt","w+")
            def myjob():
                print('hello')
            # trigger_time = datetime.datetime.now() + datetime.timedelta(seconds=50)
            # scheduler.add_job(_trigger_command, "interval", seconds=20, id=str(schedule.id))
            scheduler.add_job(_trigger_command, trigger='cron', minute='*')
        transaction.on_commit(add_processing_job)
        # try:
        #     # This is here to simulate application activity (which keeps the main thread alive).
        #     while True:
        #         time.sleep(2)
        # except (KeyboardInterrupt, SystemExit):
        #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
        #     scheduler.shutdown()


        print 'printing jobs.........'
        print scheduler.print_jobs()
        print 'doing jobs..........'
        return schedule

    def tick():
        print('Tick! The time is......####&&&&&: %s' % datetime.datetime.now())


    def _trigger_command(self):
        print '_trigger_command.....'
        f= open("/Users/dm029579/Desktop/SAP_assingment_2/my_files/yayyyyy.txt","w+")
        
        # command = ["bash","/Users/dm029579/Desktop/SAP_assingment/Scheduler/scheduler_api/bash_script2.sh"]
        # try:
        #     process = Popen(command, stdout=PIPE, stderr=STDOUT)
        #     output = process.stdout.read()
        #     exitstatus = process.poll()
        #     if (exitstatus==0):
        #             result = {"status": "Success", "output":str(output)}
        #     else:
        #             result = {"status": "Failed", "output":str(output)}

        # except Exception as e:
        #     result =  {"status": "failed", "output":str(e)}





