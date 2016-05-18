# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Region, Province
from ..serializers import ProvinceSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        region_id = self.request.query_params.get('region')

        if not is_integer(region_id):
            raise serializers.ValidationError(
                'Region integer id required.'
            )
        try:
            region = Region.objects.get(pk=region_id)
        except ObjectDoesNotExist:
            raise ObjectNotFound('Region')

        return Province.objects.filter(region=region)
