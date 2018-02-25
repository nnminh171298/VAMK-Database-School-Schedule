from django.db import models
from django.urls import reverse

class Course(models.Model):
	code = models.CharField(max_length=10)
	language = models.CharField(max_length=5, blank=True, null=True)
	name = models.CharField(max_length=100)
	credit = models.IntegerField()
	semester = models.CharField(max_length=2)
	curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')

	class Meta:
		managed = False
		db_table = 'course'

	def __str__(self):
		return str(self.curriculumid) + ' - ' + str(self.credit) + 'cr' + ' - ' + self.name

	def get_absolute_url(self):
		return reverse('schedule:course_detail', kwargs={'pk': self.pk})


class CourseImplementation(models.Model):
	courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')
	roomid = models.ForeignKey('Room', models.DO_NOTHING, db_column='roomid', blank=True, null=True)
	note = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'course_implementation'

	def __str__(self):
		return self.pk + ' - ' + self.courseid


class Curriculum(models.Model):
	name = models.CharField(max_length=10)

	class Meta:
		managed = False
		db_table = 'curriculum'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('schedule:curriculum_detail', kwargs={'pk': self.pk})

class Group(models.Model):
	code = models.CharField(max_length=10)
	degree = models.CharField(max_length=5)
	curriculumid = models.ForeignKey(Curriculum, models.DO_NOTHING, db_column='curriculumid', blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'group'

	def __str__(self):
		return self.code

	def get_absolute_url(self):
		return reverse('schedule:group_detail', kwargs={'pk': self.pk})


class GroupCourseImplementation(models.Model):
	groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid', primary_key=True)
	course_implementationid = models.ForeignKey(CourseImplementation, models.DO_NOTHING, db_column='course_implementationid')

	class Meta:
		managed = False
		db_table = 'group_course_implementation'
		unique_together = (('groupid', 'course_implementationid'),)

	def __str__(self):
		return self.pk + ' - ' + self.groupid


class Room(models.Model):
	name = models.CharField(max_length=10)
	seat = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'room'

	def __str__(self):
		return self.name + ' - ' + str(self.seat) + ' seats'

	def get_absolute_url(self):
		return reverse('schedule:room_detail', kwargs={'pk': self.pk})


class Teacher(models.Model):
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=30)

	class Meta:
		managed = False
		db_table = 'teacher'

	def __str__(self):
		return self.code + ' - ' + self.name

	def get_absolute_url(self):
		return reverse('schedule:teacher_detail', kwargs={'pk': self.pk})


class TeacherCourseImplementation(models.Model):
	teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherid', primary_key=True)
	course_impleid = models.ForeignKey(CourseImplementation, models.DO_NOTHING, db_column='course_impleid')
	p1 = models.IntegerField(blank=True, null=True)
	p2 = models.IntegerField(blank=True, null=True)
	p3 = models.IntegerField(blank=True, null=True)
	p4 = models.IntegerField(blank=True, null=True)
	p5 = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'teacher_course_implementation'
		unique_together = (('teacherid', 'course_impleid'),)

	def __str__(self):
		return self.pk + ' - ' + self.teacherid
