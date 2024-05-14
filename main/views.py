from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .models import Survey_answer,Survey_question
from .forms import SignUpForm

# Create your views here.
def main_def(request):
    question_list = Survey_question.objects.order_by('-create_time')
    context = {'question_list': question_list}
    
    return render(request,'main/question_list.html',context)

def join(request):
    context = {}
    return render(request,'main/GPT/join-1.html',context)


# login setting

def register(requset):
    if requset.method == 'POST':
        form = SignUpForm(requset.POST)
        if form.is_valid():
            form.save()  # 폼의 save() 메소드를 호출하여 사용자 정보를 DB에 저장
            return redirect('login')  # 로그인 페이지로 리다이렉트

    else:
        form = SignUpForm()
    return render(requset, 'main/GPT/join-1.html', {"form": form})

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             if user:
#                 login(request,user)
#                 return redirect('home')
#         else:
#             form = CustomAuthenticationForm()
#         return render(request, 'main/GPT/login.html', {"form": form})
    
def login_view(request):
    if request.method == 'POST':
        # Handle POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect after POST
        else:
            return HttpResponse("Invalid login", status=401)
    elif request.method == 'GET':
        # Return login form
        return render(request, 'main/GPT/login.html')
    else:
        # If the method is neither GET nor POST
        return HttpResponse("Method not allowed", status=405)
