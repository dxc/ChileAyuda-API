# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, serializers

from ..libs import ObjectNotFound, is_integer
from ..models import Incident, IncidentComment
from ..serializers import IncidentCommentSerializer


class IncidentCommentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentCommentSerializer

    def get_queryset(self):
        incident_id = self.request.query_params.get('incident')

        if not is_integer(incident_id):
            raise serializers.ValidationError(
                'Incident integer id required.'
            )
        try:
            incident = Incident.objects.get(pk=incident_id)
        except ObjectDoesNotExist:
            raise ObjectNotFound('Incident')

        return IncidentComment.objects.filter(incident=incident)
