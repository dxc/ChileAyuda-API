# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Report, ReportComment
from ..serializers import ReportCommentSerializer


class ReportCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ReportCommentSerializer

    def get_queryset(self):
        report_id = self.request.query_params.get('report')

        if not is_integer(report_id):
            raise serializers.ValidationError(
                'Report integer id required.'
            )
        try:
            report = Report.objects.get(pk=report_id)
        except ObjectDoesNotExist:
            raise ObjectNotFound('Report')

        return ReportComment.objects.filter(report=report)
