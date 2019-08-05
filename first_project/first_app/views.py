from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
     my_dict = {'insert_me' : "I am from views.py in first_app"}
     return render(request, 'first_app/index.html', context=my_dict)
