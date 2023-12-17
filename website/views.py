from django.shortcuts import render
from django.http import JsonResponse
from . import isholiday
import jdatetime


# Create your views here.
def main_page(request):
    today = str(jdatetime.datetime.now())[:10]
    # today = '1402-09-27'

    status = isholiday.find_nearest_holiday(today)
    status.update({'today': today.replace('-', '/')})
    print(status)

    if status['distance'] == 0:
        status.update({'happy': 'امروز'})
        return render(request, 'happy.html', context = status)
    elif status['distance'] == 1:
        status.update({'happy': 'فردا'})
        return render(request, 'happy.html', context = status)
    else:
        return render(request, 'sad.html', context = status)

