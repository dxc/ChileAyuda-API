# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.test.testcases import TransactionTestCase

# from ..models import Media


# class TestModelMedia(TransactionTestCase):

#     fixtures = ['mediasources.json', 'media.json']

#     def test_model_media_unicode(self):
#         expected = Media.objects.get(pk=1)
#         self.assertEquals(
#             'Facebook: http://facebook.com/fake_fb_url',
#             unicode(expected)
#         )
