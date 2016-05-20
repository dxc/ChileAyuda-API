# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..models import Category
from ..serializers import CategoryWithChildrenSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoryWithChildrenSerializer
