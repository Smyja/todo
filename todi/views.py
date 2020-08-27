from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	tasks=Task.objects.all()
	context={'tasks':tasks}
    return render(request,'toditemp/todi.html',context)
