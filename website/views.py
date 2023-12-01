from django.shortcuts import render
from django.http import JsonResponse
from . import isholiday
import jdatetime


# Create your views here.
def main_page(request):
    today = str(jdatetime.datetime.now())[:10]
    status = isholiday.isholiday(today)
    print(status)
    if status:
        return render(request, 'happy.html')
    else:
        return render(request, 'sad.html')
