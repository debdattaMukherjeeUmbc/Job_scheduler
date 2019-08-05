# -*- coding: utf-8 -*-
import factory
from . import models

import datetime

class ScheduleFactory(factory.Factory):
    class Meta:
        model = models.Schedule
