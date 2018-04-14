# @Author       : panhw
# @Time         : 2018/4/14 11:01
from rest_framework import serializers
from luffy.models import DegreeCourse, Teacher, PricePolicy

class DegreeCourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = DegreeCourse
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class PricePolicySerializers(serializers.ModelSerializer):

    class Meta:
        model = PricePolicy
        fields = '__all__'

