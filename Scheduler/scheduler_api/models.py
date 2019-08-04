# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Schedule(models.Model):
    """This class represents the bucketlist model."""
    job_name = models.CharField(max_length=255, blank=False)
    job_description = models.CharField(max_length=255, blank=False)
    command = models.CharField(max_length=255, blank=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    job_frequency = models.IntegerField(default=1)
    duration = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
