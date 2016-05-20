# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from ..libs import is_integer, InvalidRequestException
from ..models import ReportComment
from ..serializers import ReportCommentSerializer


class ReportCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ReportCommentSerializer

    def get_queryset(self):
        incident_id = self.kwargs.get('incident_pk')
        report_id = self.kwargs.get('report_pk')
        comment_id = self.kwargs.get('pk')

        if is_integer(incident_id) and is_integer(report_id) and comment_id is None:
            return ReportComment.objects.filter(
                report__incident=incident_id,
                report=report_id
            )
        elif is_integer(incident_id) and is_integer(report_id) and is_integer(comment_id):
            return ReportComment.objects.filter(
                report__incident=incident_id,
                report=report_id,
                pk=comment_id
            )
        else:
            raise InvalidRequestException('Invalid parameters.')
