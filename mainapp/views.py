from django.shortcuts import render

from .forms import UserRgistrationForm

# Create your views here.

def SingUp(request):
    form = UserRgistrationForm()
    if request.method == 'POST':
        form = UserRgistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('user_login:login'))

    data = {
        "form": form,
    }
    return render(request, 'index.html', data)
