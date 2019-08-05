# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from . import updater


class SchedulerApiConfig(AppConfig):
    name = 'scheduler_api'
