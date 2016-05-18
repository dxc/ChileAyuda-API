"""chileayuda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers

from api.views.user import UserViewSet
from api.views.region import RegionViewSet
from api.views.province import ProvinceViewSet
from api.views.commune import CommuneViewSet
from api.views.disaster import DisasterViewSet
from api.views.category import CategoryViewSet
from api.views.incident import IncidentViewSet
from api.views.incidentcomment import IncidentCommentViewSet
from api.views.incidentmedia import IncidentMediaViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'User')
router.register(r'regions', RegionViewSet, 'Region')
router.register(r'provinces', ProvinceViewSet, 'Province')
router.register(r'communes', CommuneViewSet, 'Commune')
router.register(r'disasters', DisasterViewSet, 'Disaster')
router.register(r'categories', CategoryViewSet, 'Category')

router.register(r'incidents', IncidentViewSet, 'Incident')
router.register(r'incidents_comments', IncidentCommentViewSet, 'IncidentComment')
router.register(r'incidents_media', IncidentMediaViewSet, 'IncidentMedia')

urlpatterns = [
    url(r'^0/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
