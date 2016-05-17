# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

from ..models import Province, Commune
from ..serializers import CommuneSerializer


class CommuneViewSet(viewsets.ModelViewSet):
    serializer_class = CommuneSerializer

    def get_queryset(self):
        province_id = self.request.query_params.get('province')

        if province_id in [None, '', 'null']:
            return Commune.objects.none()

        try:
            province = Province.objects.get(pk=province_id)
        except ObjectDoesNotExist:
            return Commune.objects.none()

        return Commune.objects.filter(province=province)
