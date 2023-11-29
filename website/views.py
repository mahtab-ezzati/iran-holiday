from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def main_page(request):
    return JsonResponse({'date': '1402-01-01', 'holiday':'Y'})
