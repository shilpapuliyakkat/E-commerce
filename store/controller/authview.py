from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def registerview(request):
    form=CustomUserForm()
    if request.method == 'POST':
       form = CustomUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request, "Registered Successfully! Login to Continue")
          return redirect('login')
    context={'form':form}
    return render(request,"store/auth/register.html",context)


  

def loginview(request):
        
    #  if request.user.is_authenticated:
    #     messages.warning(request,"You are already logged in")
    #     return redirect('home')

        if request.method == 'POST':
           name = request.POST.get('username')
           passwd = request.POST.get('password')
           user = authenticate(request, username=name, password=passwd)
           print(name)
        
           if user is not None:
              login(request, user)
              messages.success(request, "Logged in Successfully")
              return redirect("home")
           else:
              messages.error(request, "Invalid Username or Password")
              return redirect('login')
            
        return render(request,"store/auth/login.html")
     
def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Loggout in Successfully")
    return redirect("home")

