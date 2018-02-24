from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^course/$', views.CourseView.as_view(), name='course'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course_detail'),
    url(r'^course/add/$', views.CourseCreate.as_view(), name='course-add'),
    url(r'^course/(?P<pk>[0-9]+)/update/$', views.CourseUpdate.as_view(), name='course-update'),
    url(r'^course/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),

    url(r'^teacher/$', views.TeacherView.as_view(), name='teacher'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherDetail.as_view(), name='teacher_detail'),
    url(r'^teacher/add/$', views.TeacherCreate.as_view(), name='teacher-add'),
    url(r'^teacher/(?P<pk>[0-9]+)/update/$', views.TeacherUpdate.as_view(), name='teacher-update'),
    url(r'^teacher/(?P<pk>[0-9]+)/delete/$', views.TeacherDelete.as_view(), name='teacher-delete'),

    url(r'^curriculum/$', views.CurriculumView.as_view(), name='curriculum'),
    url(r'^curriculum/(?P<pk>[0-9]+)/$', views.CurriculumDetail.as_view(), name='curriculum_detail'),
    url(r'^curriculum/add/$', views.CurriculumCreate.as_view(), name='curriculum-add'),
    url(r'^curriculum/(?P<pk>[0-9]+)/update/$', views.CurriculumUpdate.as_view(), name='curriculum-update'),
    url(r'^curriculum/(?P<pk>[0-9]+)/delete/$', views.CurriculumDelete.as_view(), name='curriculum-delete'),

    url(r'^room/$', views.RoomView.as_view(), name='room'),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view(), name='room_detail'),
    url(r'^room/add/$', views.RoomCreate.as_view(), name='room-add'),
    url(r'^room/(?P<pk>[0-9]+)/update/$', views.RoomUpdate.as_view(), name='room-update'),
    url(r'^room/(?P<pk>[0-9]+)/delete/$', views.RoomDelete.as_view(), name='room-delete'),

    url(r'^group/$', views.GroupView.as_view(), name='group'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group_detail'),
    url(r'^group/add/$', views.GroupCreate.as_view(), name='group-add'),
    url(r'^group/(?P<pk>[0-9]+)/update/$', views.GroupUpdate.as_view(), name='group-update'),
    url(r'^group/(?P<pk>[0-9]+)/delete/$', views.GroupDelete.as_view(), name='group-delete'),

    url(r'^$', RedirectView.as_view(url='course', permanent=False), name='schedule_index'),
]