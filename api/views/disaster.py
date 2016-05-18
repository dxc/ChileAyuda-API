# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..models import Disaster
from ..serializers import DisasterSerializer


class DisasterViewSet(viewsets.ModelViewSet):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer
