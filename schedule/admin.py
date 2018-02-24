from django.contrib import admin
from .models import Course, Curriculum, Group, Room, Teacher

# Register your models here.
admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Group)
admin.site.register(Room)
admin.site.register(Teacher)