from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def account_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request , username = username, password = password)
        # context = {}
        # if user == None:
        #     context['error'] = 'Invalid username or password'
        #     return render(request,'accounts/login.html',context = context)
        if form.is_valid():
            user = form.get_user() 
            login(request, user)
        return redirect('/')
    else:
         form = AuthenticationForm(request)
    return render(request,'accounts/login.html',{'form':form})


def account_logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request,'accounts/logout.html')


def account_register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
            user_obj = form.save()
            return redirect('/login/')


    return render(request,'accounts/register.html',{'form' : form})

