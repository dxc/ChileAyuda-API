# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Style, Category


class TestModelCategory(TransactionTestCase):

    fixtures = ['styles.json', 'categories.json']

    def test_model_category_unicode(self):
        expected = Category.objects.get(pk=1)
        self.assertEquals(
            'Emergencia',
            unicode(expected)
        )

        child = Category.objects.get(pk=2)
        children = expected.children.all()

        self.assertEquals(1, len(children))
        self.assertIn(child, children)

        expected = Category.objects.get(pk=3)
        children = expected.children.all()
        self.assertEquals(0, len(children))

    def test_model_category_subcategories(self):
        parent = Category.objects.get(pk=1)
        style = Style.objects.get(pk=1)

        subcategory = Category(
            name="Sub-emergencia 2",
            style=style,
            parent=parent
        )
        subcategory.save()

        self.assertIn(subcategory, parent.children.all())
