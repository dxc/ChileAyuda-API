# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Incident, Report
from ..serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer

    def get_queryset(self):
        incident_id = self.request.query_params.get('incident')

        report_id = self.kwargs.get('pk')

        if report_id is not None and is_integer(report_id):
            return Report.objects.filter(pk=report_id)
        elif is_integer(incident_id):
            try:
                incident = Incident.objects.get(pk=incident_id)
            except ObjectDoesNotExist:
                raise ObjectNotFound('Incident')

            return Report.objects.filter(incident=incident)
        raise serializers.ValidationError(
            'Incident integer id required.'
        )
