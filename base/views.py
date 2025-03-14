from django.shortcuts import render, redirect
from .models import User, DataSet
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .utils import summary, visualization


def home(request):
    return render(request, 'home.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        return redirect('home')
    return render(request, 'user_register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'user_login.html')

def upload_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            curr_user = request.user
            file = request.FILES['file']
            dataset_ins = DataSet(user=curr_user, data=file)
            dataset_ins.save()
            return redirect('home')
        return render(request, 'file_upload.html')
    return HttpResponse('You are not Authenticated.')

def file_list(request):
    context = {}
    if request.user.is_authenticated:
        curr_user = request.user
        all_data = DataSet.objects.filter(user=curr_user)
        context['all_data'] = all_data
        return render(request, 'file_list.html', context)
    return HttpResponse('You are not Authenticated')

def user_logout(request):
    logout(request)
    return redirect('home')

def interact_with_single_file(request, pk):
    context = {}
    if request.user.is_authenticated:
        dataset = DataSet.objects.get(pk=pk)
        dataset_url = dataset.data.path
        print(dataset_url)
        if request.method == 'POST':
            print(request.POST)
            summary_option = request.POST['summary-options']
            visualization_option = request.POST['visualization-options']
            
            #Analysis
            basic_column = request.POST['basic-column']
            target_column = request.POST['target-column']
            condition = request.POST['condition']
            value = request.POST['value']
            
            #Visualisation
            visual_col1 = request.POST['visual-column1']
            visual_col2 = request.POST['visual-column2']

            if summary_option != 'None':
                summary_res = summary(summary_option, dataset_url)
            if summary_option == "5":
                if basic_column != '' and target_column != '' and condition != '' and value != '':
                    summary_res = summary(summary_option, dataset_url, column=basic_column, target_column=target_column, condition=condition, value=value)


            if visualization_option != 'None':

                if visualization_option == '4' and visual_col1 != '': 
                    visualization_res = visualization(visualization_option, dataset_url, visual_column=visual_col1)

                elif visualization_option == '6' and visual_col2 != '' and visual_col1 != '':
                    visualization_res = visualization(visualization_option, dataset_url, visual_column=visual_col1, visual_column2 = visual_col2)

                else:
                    visualization_res = visualization(visualization_option, dataset_url)

            context['summary'] = summary_res
            context['visualization'] = f'/media/visualization/{visualization_res}'
            return render(request, 'single_file.html', context)
        return render(request, 'single_file.html', context)
    return HttpResponse('You are not authenticated.')
