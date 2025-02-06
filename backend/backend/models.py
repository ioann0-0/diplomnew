from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)  # 'admin', 'teacher', etc.

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  # 'present', 'absent'
    marked_at = models.DateTimeField(auto_now_add=True)

class Userr(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username