import os
from django.shortcuts import render
import glob
from .models import Place
#
# def exam(request):
#     url="https://www.grapestechs.com/pythontoscript/online_exam1/teacherindex.php"
#     return render(request, 'exam.html',{'url':url})
# views.py
from django.shortcuts import render
import subprocess

from django.http import HttpResponse

import subprocess
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def exam(request):
    if request.method == 'POST':
        print(1)
        # Run the Python code for real-time object detection and capture the output
        process = subprocess.Popen(
            ["python", "real_time_object_detection.py", "--prototxt", "MobileNetSSD_deploy.prototxt.txt", "--model",
             "MobileNetSSD_deploy.caffemodel"],
            stdout=subprocess.PIPE,
        )

        stdout= process.communicate()

        Place.objects.all().delete()
        Place.objects.create(name=stdout)

        content=stdout
        other_url = 'http://localhost:8000/malpractice/'
        requests.post(other_url, data={'content': content})
        return render(request, 'exam.html', {'stdout': content})
    else:
        return render(request, 'exam.html')


def congrats(request):
    content=Place.objects.first().name
    my_bytes = content.encode('utf-8')

    stdout = my_bytes.decode("utf-8")
    content = stdout.split("/")

    return render(request, 'result.html',{'content': content})

import requests

def Save_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        url = "https://objects-detection.p.rapidapi.com/objects-detection"
        headers = {
            "X-RapidAPI-Key": "17922e44ccmsh348879d1968daebp1b4a30jsnd0801c770809",
            "X-RapidAPI-Host": "objects-detection.p.rapidapi.com"
        }

        response = requests.post(url, files={"image": image}, headers=headers)
        result = response.json()

        # Save the uploaded image in the upload model
        img_instance = upload(image=image)
        img_instance.save()
        return render(request, 'image_page.html', {'result': result,'image': img_instance})
    return render(request, 'upload_image.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
           
            image_data = image.read()
            
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

