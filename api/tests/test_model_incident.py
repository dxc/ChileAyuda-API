# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test.testcases import TransactionTestCase

from ..models import Incident, MediaSource


class TestModelIncident(TransactionTestCase):

    fixtures = [
        'users.json',
        'regions.json',
        'provinces.json',
        'communes.json',
        'coordinates.json',
        'disasters.json',
        'styles.json',
        'categories.json',
        'media_sources.json',
        'incidents.json',
    ]

    def test_model_incident_unicode(self):
        expected = Incident.objects.get(pk=1)

        self.assertEquals(
            'Desastre de prueba en Beauchef - Incidente de prueba',
            unicode(expected)
        )

    def test_model_incident_validate(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)
        text = 'Incidente verificado en el lugar.'

        result = incident.validate(user, text)
        self.assertTrue(result)

        expected = Incident.objects.get(pk=1).incidentvalidation_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(text, expected[0].text)

    def test_model_incident_validate_invalid(self):
        incident = Incident.objects.get(pk=1)

        text = 'Incidente verificado en el lugar.'

        for args in [(None, None), (None, text)]:
            result = incident.validate(*args)
            self.assertFalse(result)

            expected = Incident.objects.get(pk=1).incidentvalidation_set.all()
            self.assertEquals(0, len(expected))

    def test_model_incident_set_details(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        details = {
            'missing_people': 1,
            'injured_people': 2,
            'damaged_buildings': 1
        }

        incident.set_details(user, details)

        expected = Incident.objects.get(pk=1).incidentdetail

        self.assertIsNotNone(expected)
        self.assertEquals(1, expected.missing_people)
        self.assertEquals(2, expected.injured_people)
        self.assertEquals(1, expected.damaged_buildings)

        self.assertIsNone(expected.deceased_people)
        self.assertIsNone(expected.damaged_vehicles)

    def test_model_incident_set_details_invalid(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        details = {
            'missing_people': 1,
        }

        args_list = [
            (None, None),
            (None, {}),
            (None, details),
            (user, None),
            (user, {}),
        ]

        for args in args_list:
            incident.set_details(*args)

            try:
                expected = Incident.objects.get(pk=1).incidentdetail
                self.fail()
            except ObjectDoesNotExist:
                expected = None
            self.assertIsNone(expected)

    def test_model_incident_rate(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        rating = 1

        incident.rate(user, rating)

        expected = Incident.objects.get(pk=1).incidentrating_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(rating, expected[0].value)

    def test_model_incident_rate_invalid(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        args_list = [
            (None, None),
            (None, 'fake_number'),
            (None, 1),
            (None, 5),
            (user, None),
            (user, 'fake_number'),
            (user, 5),
        ]

        for args in args_list:
            incident.rate(*args)

            expected = Incident.objects.get(pk=1).incidentrating_set.all()
            self.assertNotEquals(1, len(expected))

    def test_model_incident_add_comment(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        text = 'Este es un comentario de prueba'

        incident.add_comment(user, text)

        expected = Incident.objects.get(pk=1).incidentcomment_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(text, expected[0].text)

    def test_model_incident_add_comment_invalid(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)

        args_list = [
            (None, None),
            (user, None),
            (user, ''),
        ]

        for args in args_list:
            incident.add_comment(*args)

            expected = Incident.objects.get(pk=1).incidentcomment_set.all()
            self.assertNotEquals(1, len(expected))

    def test_model_incident_add_media(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)
        source = MediaSource.objects.get(pk=1)

        url = 'http://fake_url'

        incident.add_media(user, source, url)

        expected = Incident.objects.get(pk=1).incidentmedia_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(source, expected[0].source)
        self.assertEquals(url, expected[0].url)

    def test_model_incident_add_media_invalid(self):
        incident = Incident.objects.get(pk=1)
        user = User.objects.get(pk=1)
        source = MediaSource.objects.get(pk=1)

        args_list = [
            (None, None, None),
            (user, None, None),
            (user, source, None),
            (user, source, ''),
        ]

        for args in args_list:
            incident.add_media(*args)

            expected = Incident.objects.get(pk=1).incidentmedia_set.all()
            self.assertNotEquals(1, len(expected))
