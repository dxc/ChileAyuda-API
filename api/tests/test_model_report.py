# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test.testcases import TransactionTestCase

from ..models import Report, MediaSource


class TestModelReport(TransactionTestCase):

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
        'reports.json',
    ]

    def test_model_report_unicode(self):
        expected = Report.objects.get(pk=1)

        self.assertEquals(
            'Desastre de prueba en Beauchef - Reporte de prueba',
            unicode(expected)
        )

    def test_model_report_validate(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)
        text = 'Reporte verificado en el lugar.'

        result = report.validate(user, text)
        self.assertTrue(result)

        expected = Report.objects.get(pk=1).reportvalidation_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(text, expected[0].text)

    def test_model_report_validate_invalid(self):
        report = Report.objects.get(pk=1)

        text = 'Reporte verificado en el lugar.'

        for args in [(None, None), (None, text)]:
            result = report.validate(*args)
            self.assertFalse(result)

            expected = Report.objects.get(pk=1).reportvalidation_set.all()
            self.assertEquals(0, len(expected))

    def test_model_report_set_details(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)

        details = {
            'missing_people': 1,
            'injured_people': 2,
            'damaged_buildings': 1
        }

        report.set_details(user, details)

        expected = Report.objects.get(pk=1).reportdetail

        self.assertIsNotNone(expected)
        self.assertEquals(1, expected.missing_people)
        self.assertEquals(2, expected.injured_people)
        self.assertEquals(1, expected.damaged_buildings)

        self.assertIsNone(expected.deceased_people)
        self.assertIsNone(expected.damaged_vehicles)

    def test_model_report_set_details_invalid(self):
        report = Report.objects.get(pk=1)
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
            report.set_details(*args)

            try:
                expected = Report.objects.get(pk=1).reportdetail
                self.fail()
            except ObjectDoesNotExist:
                expected = None
            self.assertIsNone(expected)

    def test_model_report_rate(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)

        rating = 1

        report.rate(user, rating)

        expected = Report.objects.get(pk=1).reportrating_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(rating, expected[0].value)

    def test_model_report_rate_invalid(self):
        report = Report.objects.get(pk=1)
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
            report.rate(*args)

            expected = Report.objects.get(pk=1).reportrating_set.all()
            self.assertNotEquals(1, len(expected))

    def test_model_report_add_comment(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)

        text = 'Este es un comentario de prueba'

        report.add_comment(user, text)

        expected = Report.objects.get(pk=1).reportcomment_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(text, expected[0].text)

    def test_model_report_add_comment_invalid(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)

        args_list = [
            (None, None),
            (user, None),
            (user, ''),
        ]

        for args in args_list:
            report.add_comment(*args)

            expected = Report.objects.get(pk=1).reportcomment_set.all()
            self.assertNotEquals(1, len(expected))

    def test_model_report_add_media(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)
        source = MediaSource.objects.get(pk=1)

        url = 'http://fake_url'

        report.add_media(user, source, url)

        expected = Report.objects.get(pk=1).reportmedia_set.all()

        self.assertEquals(1, len(expected))
        self.assertEquals(user, expected[0].user)
        self.assertEquals(source, expected[0].source)
        self.assertEquals(url, expected[0].url)

    def test_model_report_add_media_invalid(self):
        report = Report.objects.get(pk=1)
        user = User.objects.get(pk=1)
        source = MediaSource.objects.get(pk=1)

        args_list = [
            (None, None, None),
            (user, None, None),
            (user, source, None),
            (user, source, ''),
        ]

        for args in args_list:
            report.add_media(*args)

            expected = Report.objects.get(pk=1).reportmedia_set.all()
            self.assertNotEquals(1, len(expected))
