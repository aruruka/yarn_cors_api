import requests as r
import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listApps(request):
    url = "http://kyan-cdh03.novalocal:8088/ws/v1/cluster/apps?deSelects=resourceRequests"
    payload={}
    headers = {}
    response = r.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    # return HttpResponse("Hello, world. You're at the yarn cors api demo listApps.")
    return HttpResponse(json.dumps(response.text, indent=4, sort_keys=True))
