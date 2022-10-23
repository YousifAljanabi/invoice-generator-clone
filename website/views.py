from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, "website/index.html")

def tempo(request):
    return render(request, "website/tempp.html")


def view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #do something
        request_data = request.POST.get('printContents')
        print((request_data))
        return HttpResponse("OK")