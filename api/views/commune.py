# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Province, Commune
from ..serializers import CommuneSerializer


class CommuneViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommuneSerializer

    def get_queryset(self):
        province_id = self.request.query_params.get('province')

        if not is_integer(province_id):
            raise serializers.ValidationError(
                'Province integer id required.'
            )
        try:
            province = Province.objects.get(pk=province_id)
        except ObjectDoesNotExist:
            raise ObjectNotFound('Province')

        return Commune.objects.filter(province=province)
