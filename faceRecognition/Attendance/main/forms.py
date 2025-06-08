from django import forms

class markAttendanceForm(forms.Form):
    studentNum = forms.CharField(label="Student number:")
    imageData = forms.CharField(widget=forms.HiddenInput())
