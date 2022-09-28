from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserRgistrationForm

# Create your views here.

def SingUp(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already registerUser !')
        return redirect('dashboard')
    elif request.method == 'POST':
        form = UserRgistrationForm(request.POST)

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confrim_password=request.POST['confrim_password']
        if password == confrim_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username Already  taken ')
                # return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email Already taken')
                # return redirect('register')

            elif form.is_valid():
            # ei vabe save korle 
            #Invalid password format or unknown hashing algorithm.
            # form.save()
            # so ei vabe save korlam 
            # first_name=form.cleaned_data['first_name']
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.is_staff=True
                user.save() 
                messages.info(request,'successfully create your account ')
                return redirect('login')
           
            else:
                print("invalid")
                print(form.errors)
            # ei khane redireect kora jabe na ...korle problem hobe 
            
          
        else:
            messages.info(request,'Password Not Matching ,please try again ! ')
            # return redirect('register')


         
    else:
        form = UserRgistrationForm()
    data = {
        "form": form,
    }
    return render(request, 'mainapp/register.html', data)


def Login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already Login !')
        return redirect('dashboard')
    elif request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
       
         # is_activate is ture then login 
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Login your account .')
            return redirect('dashboard')
        # Redirect to a success page.
        else:
            messages.error(request, 'Email or Password not match . please try again !')
            return redirect('login')
    
    return render(request, 'mainapp/login.html')


def LogOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'successfully logout !')
        return redirect('login')
    else:
        messages.warning(request, 'Please login before logging out! !')
        return redirect('login')
     
  

def Dashboard(request):
    return render(request, 'mainapp/profile.html')




            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # username=form.cleaned_data['username']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # confrim_password=form.cleaned_data['confrim_password']
            # user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            # user.save() 
