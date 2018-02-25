from .models import Course, Curriculum, Room, Group, Teacher
from .forms import UserForm
from .serializers import CourseSerializer, CurriculumSerializer, RoomSerializer, GroupSerializer, TeacherSerializer
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
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