from django.urls import path
from backend.views import UserViewSet, ScheduleViewSet, AttendanceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'schedule', ScheduleViewSet, basename='schedule')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls
