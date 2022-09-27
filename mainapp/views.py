from django.shortcuts import render,redirect

from .forms import UserRgistrationForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def SingUp(request):
    if request.method == 'POST':
        form = UserRgistrationForm(request.POST)
        print("post")
        if form.is_valid():
            print("Rgister page  save before")
            form.save()
            print("Rgister page ")
            # return HttpResponseRedirect(reverse('user_login:login'))
        else:
            print("invalid")
            print(form.errors)
         
    else:
        form = UserRgistrationForm()
    data = {
        "form": form,
    }
    return render(request, 'register.html', data)


def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
       
         # is_activate is ture then login 
        if user is not None:
            login(request, user)
            print("successfully login ")
            return redirect('dashboard')
        # Redirect to a success page.
        else:
            print("user is not found ")
            # messages.error(request, 'email or password not match . please try again !')
            return redirect('login')
    
    return render(request, 'login.html')


def LogOut(request):
    logout(request)
    # messages.error(request, 'successfully login out  !')
    return redirect('login')

def Dashboard(request):
    return render(request, 'profile.html')




            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # username=form.cleaned_data['username']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # confrim_password=form.cleaned_data['confrim_password']
            # user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            # user.save() 