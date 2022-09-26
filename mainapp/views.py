from django.shortcuts import render

from .forms import UserRgistrationForm

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
    return render(request, 'index.html', data)




            # first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            # username=form.cleaned_data['username']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # confrim_password=form.cleaned_data['confrim_password']
            # user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            # user.save() 