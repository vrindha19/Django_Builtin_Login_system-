from django.shortcuts import render,redirect

from django.contrib.auth. forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout


def login_view(request):
   if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)
         if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
         else:
             form = AuthenticationForm()
             return render(request, 'app4/login.html', {'form': form})
def index(request):
    return render(request, 'index.html')
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the home page after logout

