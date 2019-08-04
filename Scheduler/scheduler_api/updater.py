import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
# from django_apscheduler.jobstores import register_events, register_job

from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler()

def start():
    # if settings.DEBUG:
    #   	# Hook into the apscheduler logger
    #     logging.basicConfig(filename='/tmp/log', level=logging.DEBUG, format='[%(asctime)s]: %(levelname)s : %(message)s')
    #     logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    # Add the scheduled jobs to the Django admin interface
    # register_events(scheduler)

    scheduler.start()