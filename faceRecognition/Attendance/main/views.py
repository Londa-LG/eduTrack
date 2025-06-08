import os
from django.shortcuts import render
import base64
from .forms import markAttendanceForm
from .confirm_identity import checkIdentity

# General views
def logout(request):
    pass

# Student views
def markAttendance(request):
    if request.method == 'POST':
        form = markAttendanceForm(request.POST)
        if form.is_valid():
            image_data = form.cleaned_data["imageData"]
            stdNumb = form.cleaned_data["studentNum"]

            if image_data:
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]

                image_binary = base64.b64decode(imgstr)

                filename = f"{stdNumb}_unknown.png"
                file_path = f"./main/unknown/{filename}"

                with open(file_path, 'wb') as f:
                    f.write(image_binary)

                # Confirm identity
                iden = checkIdentity(stdNumb,file_path)

                if iden == True:
                    # delete unkown image
                    os.remove(file_path)
                    # Login
                    # create session
                    # redirect to dashboard
                    return render(request, 'identified.html',{'message': stdNumb})
                else:
                    # delete unkown image
                    os.remove(file_path)
                    # stay on atendance page
                    # Return error message
                    return render(request, 'wrong.html',{'message': "You're not who you say you are"})
    else:
        
        context = {
            "form": markAttendanceForm(),
        }
        return render(request, 'markAttendance.html',context)

def studentDashboard(request):
    context = {

    }
    return render(request, 'studentDashboard.html',context)

# Lecturer views
def lecturerDashboard(request):
    context = {

    }
    return render(request, 'lecturerDashboard.html',context)

def lecturerLogin(request):
    context = {

    }
    return render(request, 'lecturerLogin.html',context)
