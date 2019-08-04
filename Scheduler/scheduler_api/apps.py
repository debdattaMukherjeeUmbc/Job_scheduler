# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class SchedulerApiConfig(AppConfig):
    name = 'scheduler_api'

    def ready(self):
        from . import updater
        updater.start()