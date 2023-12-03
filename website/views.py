from django.shortcuts import render
from django.http import JsonResponse
from . import isholiday
import jdatetime


# Create your views here.
def main_page(request):
    today = str(jdatetime.datetime.now())[:10]
    status = isholiday.find_nearest_holiday(today)
        
    return render(request, 'happy.html', context={'status' : status})

