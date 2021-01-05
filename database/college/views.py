#from django.shortcuts import redirect, render
#from .models import College
#from .forms import College CreationForm
#from django.contrib import messages
from django.http.response import HttpResponseNotFound


# Create your views here.
def home(request):
    #college = College.objects.all()
    #return render(request, 'college/home.html', {'data': college})
    return HttpResponse("hi")
