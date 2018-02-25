from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView
from schedule import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'curriculums', views.CurriculumViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('schedule/', include('schedule.urls'), name = 'schedule'),
    path('REST', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', RedirectView.as_view(url='schedule', permanent=False), name = 'vamk_index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)