# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Region, Province, Commune, Coordinates, Disaster, Style, \
                    Category, MediaSource, IncidentMedia, IncidentDetail,    \
                    IncidentValidation, IncidentRating, IncidentComment,     \
                    Incident


class RecursiveField(serializers.Serializer):

    def to_native(self, value):
        return self.parent.to_native(value)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class RegionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'name', 'iso_3166_2')


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Province
        fields = ('id', 'name')


class ProvinceWithRegionSerializer(serializers.HyperlinkedModelSerializer):

    region = RegionSerializer()

    class Meta:
        model = Province
        fields = ('id', 'name', 'region')


class CommuneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Commune
        fields = ('id', 'name')


class CommuneWithProvinceSerializer(serializers.HyperlinkedModelSerializer):

    province = ProvinceWithRegionSerializer()

    class Meta:
        model = Commune
        fields = ('id', 'name', 'province')


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):

    latitude = serializers.DecimalField(
        max_digits=9,
        decimal_places=7,
        coerce_to_string=False
    )
    longitude = serializers.DecimalField(
        max_digits=10,
        decimal_places=7,
        coerce_to_string=False
    )

    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude')


class DisasterSerializer(serializers.HyperlinkedModelSerializer):

    coordinates = CoordinatesSerializer()
    commune = CommuneWithProvinceSerializer()
    user = UserSerializer()

    class Meta:
        model = Disaster
        fields = (
            'name',
            'description',
            'user',
            'date',
            'commune',
            'coordinates'
        )


class StyleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Style
        fields = ('name', 'color')


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    parent = RecursiveField()
    style = StyleSerializer()

    class Meta:
        model = Category
        fields = ('name', 'parent', 'style')


class MediaSourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MediaSource
        fields = ('name',)


class IncidentValidationSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = IncidentValidation
        fields = ('user', 'date', 'text')


class IncidentDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IncidentDetail
        fields = (
            'missing_people',
            'injured_people',
            'deceased_people',
            'damaged_buildings',
            'damaged_vehicles'
        )


# TODO: Check
class IncidentRatingSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = IncidentRating
        fields = ('user', 'date', 'value')


class IncidentCommentSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = IncidentComment
        fields = ('user', 'date', 'text')


class IncidentMediaSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()
    source = MediaSourceSerializer()

    class Meta:
        model = IncidentMedia
        fields = ('user', 'date', 'source', 'url')


class IncidentSerializer(serializers.HyperlinkedModelSerializer):

    disaster = DisasterSerializer()
    categories = CategorySerializer(many=True)

    user = UserSerializer()

    commune = CommuneSerializer()
    coordinates = CoordinatesSerializer()

    class Meta:
        model = Incident
        fields = (
            'disaster',
            'categories',
            'name',
            'description',
            'date',
            'user',
            'commune',
            'coordinates'
        )
