# -*- coding: utf-8 -*-
import factory
from . import models

import datetime

class ScheduleFactory(factory.Factory):
    class Meta:
        model = models.Schedule

    # job_name = 'My first job'
    # command = 'echo hi diya'
    # schedule_time = datetime.datetime.now()