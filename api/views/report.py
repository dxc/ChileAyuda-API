# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..libs import is_integer, InvalidRequestException
from ..models import Report
from ..serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = ReportSerializer

    def get_queryset(self):
        incident_id = self.kwargs.get('incident_pk')
        report_id = self.kwargs.get('pk')

        if is_integer(incident_id) and report_id is None:
            return Report.objects.filter(incident=incident_id)
        elif is_integer(incident_id) and is_integer(report_id):
            return Report.objects.filter(incident=incident_id, pk=report_id)
        else:
            raise InvalidRequestException('Invalid parameters.')
