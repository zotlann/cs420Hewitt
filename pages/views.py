from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.

def Login(request):
    #if we get login form data, try to authenticate user and redirect to home
    if request.method == 'POST':
        print("EARLY TEST")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)

    #if the user is already logged in, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('home')
    #otherwise show them the login page
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def Home(request):
    return render(request,'home.html')

def CreateAccount(request):
    #if we recieved the user account creation data in the form,
    #create the user and show a screen to indicate successful 
    #account creation
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Home)
        else:
            return HttpResponse('Account Creation Failed')
    else:
        form = UserCreationForm()
        return render(request, 'create_account.html',{'form':form})


def Recipes(request):
    return render(request, 'recipes.html')

def Chicken(request):
    return render(request, 'recipes/chk.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

