from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
# Create your views here.

def index(request):
    my_dict = {"challenge" : "This is Help Page"}
    return render(request, 'second_app/index.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('id')
    user_dict = {'user_records': user_list}
    return render(request, 'second_app/users.html', context=user_dict)
