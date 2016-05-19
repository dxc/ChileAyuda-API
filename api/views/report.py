# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Disaster, Report
from ..serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer

    def get_queryset(self):
        disaster_id = self.request.query_params.get('disaster')

        if not is_integer(disaster_id):
            raise serializers.ValidationError(
                'Disaster integer id required.'
            )
        try:
            disaster = Disaster.objects.get(pk=disaster_id)
        except ObjectDoesNotExist:
            raise ObjectNotFound('Disaster')

        return Report.objects.filter(disaster=disaster)
