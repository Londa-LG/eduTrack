from django.db import models
from django.contrib.auth.models import User

class lecturer(User):
    staffNumber = models.CharField(max_length=100,primary_key=True)

    class Meta:
        verbose_name_plural ="Lecturers"

    def __str__():
        return self.staffNumber

class student(User):
    studentNumber = models.CharField(max_length=100,primary_key=True)
    imagePath = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural ="Students"

    def __str__():
        return self.studentNumber

class subject(models.Model):
    subjectCode = models.CharField(max_length=100,primary_key=True)
    subjectName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    departmentCode = models.CharField(max_length=100)

class studentSubject(models.Model):
    uniqueID = models.BigAutoField(primary_key=True)
    studentNumber = models.ForeignKey(student, on_delete = models.CASCADE)
    subjectCode = models.ForeignKey(subject, on_delete = models.CASCADE)

class subjectLecturer(models.Model):
    uniqueID = models.BigAutoField(primary_key=True)
    staffNumber = models.ForeignKey(lecturer, on_delete = models.CASCADE)
    subjectCode = models.ForeignKey(subject, on_delete = models.CASCADE)

class attendanceRecord(models.Model):
    uniqueID = models.BigAutoField(primary_key=True)
    studentNumber = models.ForeignKey(student, on_delete = models.CASCADE)
    subjectCode = models.ForeignKey(subject, on_delete = models.CASCADE)
    dateAndTime = models.DateTimeField(auto_now_add=True)
