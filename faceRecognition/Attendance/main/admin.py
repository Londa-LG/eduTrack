from django.contrib import admin
from .models import lecturer, student, subject, studentSubject, subjectLecturer, attendanceRecord

admin.site.register(lecturer)
admin.site.register(student)
admin.site.register(subject)
admin.site.register(studentSubject)
admin.site.register(subjectLecturer)
admin.site.register(attendanceRecord)
