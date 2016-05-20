# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Region, Province, Commune, Coordinates, Incident, \
                    Category, MediaSource, ReportMedia, ReportDetail, \
                    ReportValidation, ReportRating, ReportComment,    \
                    Report, Style


class RecursiveField(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


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
        fields = ('id', 'latitude', 'longitude')


class IncidentSerializer(serializers.HyperlinkedModelSerializer):

    coordinates = CoordinatesSerializer()
    commune = CommuneWithProvinceSerializer()
    user = UserSerializer()

    class Meta:
        model = Incident
        fields = (
            'id',
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
        fields = ('id', 'name', 'color')


class CategoryWithParentSerializer(serializers.ModelSerializer):

    style = StyleSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'style', 'parent')
        depth = 2


class CategoryWithChildrenSerializer(serializers.HyperlinkedModelSerializer):

    children = RecursiveField(many=True)
    style = StyleSerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'style', 'children')


class MediaSourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MediaSource
        fields = ('id', 'name',)


class ReportValidationSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ReportValidation
        fields = ('id', 'user', 'date', 'text')


class ReportDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ReportDetail
        fields = (
            'missing_people',
            'injured_people',
            'deceased_people',
            'damaged_buildings',
            'damaged_vehicles'
        )


# TODO: Check
class ReportRatingSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ReportRating
        fields = ('id', 'user', 'date', 'value')


class ReportCommentSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ReportComment
        fields = ('id', 'user', 'date', 'text')


class ReportMediaSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()
    source = MediaSourceSerializer()

    class Meta:
        model = ReportMedia
        fields = ('id', 'user', 'date', 'source', 'url')


class ReportSerializer(serializers.HyperlinkedModelSerializer):

    incident = IncidentSerializer()
    categories = CategoryWithParentSerializer(many=True)

    user = UserSerializer()

    commune = CommuneWithProvinceSerializer()
    coordinates = CoordinatesSerializer()

    class Meta:
        model = Report
        fields = (
            'id',
            'incident',
            'categories',
            'name',
            'description',
            'date',
            'user',
            'commune',
            'coordinates'
        )
