# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from factories import ScheduleFactory

class ScheduleModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def test_model_can_create_a_schedule(self):
        """Test the Schedule model can create a Schedule."""
        schedule_time = datetime.datetime.now()
        schedule = ScheduleFactory(job_name = 'My first job', command = 'echo hi diya', schedule_time = schedule_time)

        self.assertEqual(schedule.job_name, 'My first job')
        self.assertEqual(schedule.command, 'echo hi diya')
        self.assertEqual(schedule.schedule_time, schedule_time)


class ScheduleViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_api_create_a_schedule(self):
        """When posted with valid data, create should return a created/success response code."""
        schedule_time = datetime.datetime.now()
        self.schedule_data = {"job_name": "My first job", "command": "echo hello", "schedule_time": schedule_time}
        self.response = self.client.post(
            reverse('list_create'),
            self.schedule_data,
            format="json")
        
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_cannot_create_a_schedule(self):
        """When posted with  invalid data, create should return a bad request response code."""
        schedule_time = datetime.datetime.now()
        self.schedule_data = {"job_name": "My first job", "command": "echo hello"}
        self.response = self.client.post(
            reverse('list_create'),
            self.schedule_data,
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_can_get_a_schedule(self):
    	"""Get should return success status code."""
        self.response = self.client.get(reverse('list_create'))
        
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

