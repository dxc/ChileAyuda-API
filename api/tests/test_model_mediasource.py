# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import MediaSource


class TestModelMediaSource(TransactionTestCase):

    fixtures = ['media_sources.json']

    def test_model_mediasource_unicode(self):
        expected = MediaSource.objects.get(pk=1)
        self.assertEquals('Facebook', unicode(expected))
