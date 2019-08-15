from django.shortcuts import render
from django.http import HttpResponse
# from second_app.models import User
from second_app.forms import NewUserForm
# Create your views here.

def index(request):
    my_dict = {"challenge" : "This is Help Page"}
    return render(request, 'second_app/index.html', context=my_dict)

#
# def users(request):
#     user_list = User.objects.order_by('id')
#     user_dict = {'user_records': user_list}
#     return render(request, 'second_app/users.html', context=user_dict)

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form invalid')

    return render(request, 'second_app/users.html', {'form':form})
