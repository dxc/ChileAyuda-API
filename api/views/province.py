# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

from ..models import Region, Province
from ..serializers import ProvinceSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        region_id = self.request.query_params.get('region')

        if region_id in [None, '', 'null']:
            return Province.objects.none()

        try:
            region = Region.objects.get(pk=region_id)
        except ObjectDoesNotExist:
            return Province.objects.none()

        return Province.objects.filter(region=region)
