from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loginApp.forms import InsertDataForm, LoginForm
from loginApp.serializers import DataSerializer
from .models import User, Data

fee = 0.1


@csrf_exempt
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return redirect('/result')
        else:
            form = LoginForm()
            messages.info(request, 'Wrong password/username')
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@csrf_exempt
def insert_data(request):
    if request.method == "GET":
        form = InsertDataForm()
        return render(request, 'insertData.html', {'form': form})
    if request.method == "POST":
        form = InsertDataForm(request.POST)
        if form.is_valid():
            data = form.save()
            messages.info(request, 'Your data has been saved successfully!')
            form = InsertDataForm()
            return render(request, 'insertData.html', {'form': form})
        else:
            messages.info(request, 'Please Insert Valid data!')
            form = InsertDataForm()
            return render(request, 'insertData.html', {'form': form})


@csrf_exempt
@login_required(login_url='/login/')
@api_view(['GET'])
def result_api(request):
    if request.method == 'GET':
        branch = int(User.objects.get(username=request.user).branch)
        final_list = []
        if branch == 0:
            branch_objs = Data.objects.all()
        else:
            branch_objs = Data.objects.filter(branchCode=branch)
        try:
            for obj in branch_objs:
                data_serializer = DataSerializer(instance=obj)
                temp_dic = data_serializer.data
                temp_dic['کدملی'] = temp_dic['idNumber']
                temp_dic['کد شعبه'] = temp_dic['branchCode']
                temp_dic['کارمزد'] = temp_dic['transactionValue'] * fee
                temp_dic.pop('branchCode')
                temp_dic.pop('idNumber')
                temp_dic.pop('transactionValue')
                final_list.append(temp_dic)
        except ValueError:
            final_list.append({None: 'There is no data'})

        return Response(data={'result': final_list}, status=200)
