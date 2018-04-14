"""luffycity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from luffy import views
from rest_framework import routers
from luffy.views import DegreeCourseViewSet, TeacherViewSet, PricePolicyViewSet

router = routers.DefaultRouter()
router.register('degree_courses', DegreeCourseViewSet)
router.register('teachers', TeacherViewSet)
router.register('price_policies', PricePolicyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('index/', views.Index.as_view(), name='index')
]

