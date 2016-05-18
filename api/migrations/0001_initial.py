# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Commune')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Coordinates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('categories', models.ManyToManyField(to='api.Category')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Commune')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Coordinates')),
                ('disaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Disaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Incident')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missing_people', models.IntegerField(blank=True, null=True)),
                ('injured_people', models.IntegerField(blank=True, null=True)),
                ('deceased_people', models.IntegerField(blank=True, null=True)),
                ('damaged_buildings', models.IntegerField(blank=True, null=True)),
                ('damaged_vehicles', models.IntegerField(blank=True, null=True)),
                ('incident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('url', models.URLField(max_length=2000)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.IntegerField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Incident')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Incident')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('iso_3166_2', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='province',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Region'),
        ),
        migrations.AddField(
            model_name='incidentmedia',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MediaSource'),
        ),
        migrations.AddField(
            model_name='incidentmedia',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commune',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Province'),
        ),
        migrations.AddField(
            model_name='category',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Style'),
        ),
    ]
