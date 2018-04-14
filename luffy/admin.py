from django.contrib import admin

from luffy.models import PricePolicy, DegreeCourse, Teacher
# Register your models here.

admin.site.register(DegreeCourse)
admin.site.register(Teacher)
admin.site.register(PricePolicy)