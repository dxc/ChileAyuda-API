# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import viewsets

from ..serializers import UserSerializer


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.user.id

        if user_id is None:
            return User.objects.none()
        return User.objects.filter(pk=user_id)
