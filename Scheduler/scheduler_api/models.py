# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Schedule(models.Model):
    """This class represents the Schedule model."""
    job_name = models.CharField(max_length=255, blank=False)
    command = models.CharField(max_length=255, blank=False)
    schedule_time = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
