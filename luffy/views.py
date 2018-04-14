

from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet

from luffy.models import DegreeCourse, Teacher, PricePolicy
from luffy.service.serializers import DegreeCourseSerializers, TeacherSerializers, PricePolicySerializers

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        pass


class DegreeCourseViewSet(ModelViewSet):
    queryset = DegreeCourse.objects.all()
    serializer_class = DegreeCourseSerializers


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializers


class PricePolicyViewSet(ModelViewSet):
    queryset = PricePolicy.objects.all().order_by('-id')
    serializer_class = PricePolicySerializers

