from rest_framework import serializers
from .models import Course, Curriculum, Room, Group, Teacher

class CourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Course
		fields = '__all__'

class CurriculumSerializer(serializers.ModelSerializer):

	class Meta:
		model = Curriculum
		fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):

	class Meta:
		model = Room
		fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = Group
		fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Teacher
		fields = '__all__'