import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
# from django_apscheduler.jobstores import register_events, register_job

from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler()

def start():
    if settings.DEBUG:
      	# Hook into the apscheduler logger
        logging.basicConfig(filename='/tmp/log', level=logging.DEBUG, format='[%(asctime)s]: %(levelname)s : %(message)s')
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    # Adding this job here instead of to crons.
    # This will do the following:
    # - Add a scheduled job to the job store on application initialization
    # - The job will execute a model class method at midnight each day
    # - replace_existing in combination with the unique ID prevents duplicate copies of the job
    scheduler.add_job("scheduler_api.serializers.ScheduleSerializer._trigger_command", "cron", id="my_class_method", hour=0, replace_existing=True)

    # Add the scheduled jobs to the Django admin interface
    # register_events(scheduler)

    scheduler.start()