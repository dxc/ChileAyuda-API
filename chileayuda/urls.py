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
from api.views.region import RegionSet
from api.views.province import ProvinceViewSet
from api.views.commune import CommuneViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'User')
router.register(r'regions', RegionSet, 'Region')
router.register(r'provinces', ProvinceViewSet, 'Province')
router.register(r'communes', CommuneViewSet, 'Commune')

urlpatterns = [
    url(r'^0/', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
