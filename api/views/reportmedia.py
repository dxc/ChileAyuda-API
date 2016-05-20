# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..libs import is_integer, InvalidRequestException
from ..models import ReportMedia
from ..serializers import ReportMediaSerializer


class ReportMediaViewSet(viewsets.ModelViewSet):
    serializer_class = ReportMediaSerializer

    def get_queryset(self):
        incident_id = self.kwargs.get('incident_pk')
        report_id = self.kwargs.get('report_pk')
        media_id = self.kwargs.get('pk')

        if is_integer(incident_id) and is_integer(report_id) and media_id is None:
            return ReportMedia.objects.filter(
                report__incident=incident_id,
                report=report_id
            )
        elif is_integer(incident_id) and is_integer(report_id) and is_integer(media_id):
            return ReportMedia.objects.filter(
                report__incident=incident_id,
                report=report_id,
                pk=media_id
            )
        else:
            raise InvalidRequestException('Invalid parameters.')
