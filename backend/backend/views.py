from rest_framework import viewsets
from backend.models import User, Schedule, Attendance
from backend.serializers import UserSerializer, ScheduleSerializer, AttendanceSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API для работы с пользователями"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    """API для работы с расписанием"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    """API для учёта посещаемости"""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
