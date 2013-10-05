from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'diaglitica/index.html')
	
def analytics(request):
    return render(request, 'diaglitica/base_analytics.html')
