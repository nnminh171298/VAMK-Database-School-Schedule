from .models import Course, Curriculum, Room, Group, Teacher, CourseImplementation, TeacherCourseImplementation, GroupCourseImplementation
from .forms import UserForm
from .serializers import CourseSerializer, CurriculumSerializer, RoomSerializer, GroupSerializer, TeacherSerializer
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

#Course
class CourseView(generic.ListView):
	template_name = 'schedule/course.html'
	context_object_name = 'all_courses'

	def get_queryset(self):
		return Course.objects.all()

class CourseDetail(generic.DetailView):
	model = Course
	template_name = 'schedule/course_detail.html'

class CourseCreate(CreateView):
	model = Course
	fields = ['code', 'language', 'name', 'credit', 'semester', 'curriculumid']

class CourseUpdate(UpdateView):
	model = Course
	fields = ['code', 'language', 'name', 'credit', 'semester', 'curriculumid']

class CourseDelete(DeleteView):
	model = Course
	success_url = reverse_lazy('schedule:course')

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#Curriculum
class CurriculumView(generic.ListView):
	template_name = 'schedule/curriculum.html'
	context_object_name = 'all_curriculums'

	def get_queryset(self):
		return Curriculum.objects.all()

class CurriculumDetail(generic.DetailView):
	model = Curriculum
	template_name = 'schedule/curriculum_detail.html'

class CurriculumCreate(CreateView):
	model = Curriculum
	fields = ['name']

class CurriculumUpdate(UpdateView):
	model = Curriculum
	fields = ['name']

class CurriculumDelete(DeleteView):
	model = Curriculum
	success_url = reverse_lazy('schedule:curriculum')

class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

#Room
class RoomView(generic.ListView):
	template_name = 'schedule/room.html'
	context_object_name = 'all_rooms'

	def get_queryset(self):
		return Room.objects.all()

class RoomDetail(generic.DetailView):
	model = Room
	template_name = 'schedule/room_detail.html'
	
class RoomCreate(CreateView):
	model = Room
	fields = ['name', 'seat']

class RoomUpdate(UpdateView):
	model = Room
	fields = ['name', 'seat']

class RoomDelete(DeleteView):
	model = Room
	success_url = reverse_lazy('schedule:room')

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#Group
class GroupView(generic.ListView):
	template_name = 'schedule/group.html'
	context_object_name = 'all_groups'

	def get_queryset(self):
		return Group.objects.all()

class GroupDetail(generic.DetailView):
	model = Group
	template_name = 'schedule/group_detail.html'
	
class GroupCreate(CreateView):
	model = Group
	fields = ['code', 'degree', 'curriculumid']

class GroupUpdate(UpdateView):
	model = Group
	fields = ['code', 'degree', 'curriculumid']

class GroupDelete(DeleteView):
	model = Group
	success_url = reverse_lazy('schedule:group')

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#Teacher
class TeacherView(generic.ListView):
	template_name = 'schedule/teacher.html'
	context_object_name = 'all_teachers'

	def get_queryset(self):
		return Teacher.objects.all()

class TeacherDetail(generic.DetailView):
	model = Teacher
	template_name = 'schedule/teacher_detail.html'

class TeacherCreate(CreateView):
	model = Teacher
	fields = ['code', 'name']

class TeacherUpdate(UpdateView):
	model = Teacher
	fields = ['code', 'name']

class TeacherDelete(DeleteView):
	model = Teacher
	success_url = reverse_lazy('schedule:teacher')

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#Registration
class UserFormView(View):
	form_class = UserForm
	template_name = 'schedule/registration_form.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('schedule:schedule_index')
		return render(request, self.template_name, {'form': form})

#Implementation
class ImplementView(generic.ListView):
	template_name = 'schedule/implement.html'
	context_object_name = 'all_implements'

	def get_queryset(self):
		return CourseImplementation.objects.all().prefetch_related('teachercourseimplementation_set', 'groupcourseimplementation_set')

class ImplementDetail(generic.DetailView):
	model = CourseImplementation
	template_name = 'schedule/implement_detail.html'

class ImplementCreate(CreateView):
	model = CourseImplementation
	fields = ['courseid', 'roomid', 'note']

class ImplementTeacherCreate(CreateView):
	model = TeacherCourseImplementation
	fields = ['course_impleid','teacherid', 'p1', 'p2', 'p3', 'p4', 'p5']
	
	def get_initial(self):
		course = get_object_or_404(CourseImplementation, pk=self.kwargs.get('pk'))
		return {'course_impleid':course,}

class ImplementGroupCreate(CreateView):
	model = GroupCourseImplementation
	fields = ['course_implementationid', 'groupid']

	def get_initial(self):
		course = get_object_or_404(CourseImplementation, pk=self.kwargs.get('pk'))
		return {'course_implementationid':course,}

class ImplementDelete(DeleteView):
	model = CourseImplementation
	success_url = reverse_lazy('schedule:implement')

#report
def ReportIndex(request):
	return render(request, 'schedule/report_index.html')

def ReportTeacherYear(request):
	teachers = Teacher.objects.all()
	implements = TeacherCourseImplementation.objects.all()
	arr_hours = []
	for t in teachers:
		total_hours = 0
		for i in implements:
			if t.pk == i.teacherid.id:
				total_hours = sum(filter(None, [i.p1, i.p2, i.p3, i.p4, i.p5]))
				arr_hours.append(total_hours)
		if total_hours == 0:
			arr_hours.append(total_hours)
	context = {
		'teachers': teachers,
		'hours': arr_hours
	}	
	return render(request, 'schedule/report_teacher_year.html', context)

def ReportGroupDegree(request):
	groups = Group.objects.all()
	arr_indexes = []
	prev_degree = ""
	for g in groups:
		if g.degree != prev_degree:
			index = 0
		else:
			index += 1
		arr_indexes.append(index)
		prev_degree = g.degree
	context = {
		'groups': groups,
		'indexes': arr_indexes
	}
	return render(request, 'schedule/report_group_degree.html', context)

def ReportTeacherWeek(request):
	teachers = Teacher.objects.all()
	implements = TeacherCourseImplementation.objects.all()
	arr_hours = []
	for t in teachers:
		teach = 0
		for i in implements:
			if t.pk == i.teacherid.id:
				teach = 1
				arr_hours.append(i)
		if teach == 0:
			for x in range(0, 6):
				arr_hours.append(0)
	context = {
		'teachers': teachers,
		'implements': arr_hours
	}	
	return render(request, 'schedule/report_teacher_week.html', context)