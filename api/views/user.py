# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import viewsets, serializers

from ..libs import is_integer
from ..serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')

        if not is_integer(user_id):
            raise serializers.ValidationError(
                'User integer id required.'
            )
        return User.objects.filter(pk=user_id)
