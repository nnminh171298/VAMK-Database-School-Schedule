from django.conf.urls import url
from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.CourseView.as_view(), name='index'),
    
    url(r'^course/$', views.CourseView.as_view(), name='course'),
    url(r'^teacher/$', views.TeacherView.as_view(), name='teacher'),
    url(r'^curriculum/$', views.CurriculumView.as_view(), name='curriculum'),
    url(r'^room/$', views.RoomView.as_view(), name='room'),
    url(r'^group/$', views.GroupView.as_view(), name='group'),
    
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course_detail'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherDetail.as_view(), name='teacher_detail'),
    url(r'^curriculum/(?P<pk>[0-9]+)/$', views.CurriculumDetail.as_view(), name='curriculum_detail'),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view(), name='room_detail'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group_detail'),
    
    url(r'^course/add/$', views.CourseCreate.as_view(), name='course-add'),
    url(r'^teacher/add/$', views.TeacherCreate.as_view(), name='teacher-add'),
    url(r'^curriculum/add/$', views.CurriculumCreate.as_view(), name='curriculum-add'),
    url(r'^room/add/$', views.RoomCreate.as_view(), name='room-add'),
    url(r'^group/add/$', views.GroupCreate.as_view(), name='group-add'),
]