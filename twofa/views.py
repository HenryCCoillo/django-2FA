from django.shortcuts import render,redirect
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import logout

from django.contrib import messages
from .forms import RegisterForm
class Home(View):
    def get(self,request):
        return render(request, 'home.html')
    

class Login(View):
    def get(self,request):
        return render(request, 'Login/login.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'Login/signup.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/dashboard/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='two_factor:login')

        return render(request, self.template_name, {'form': form})



def SignOff(request):
    logout(request)
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self,request):
        return render(request, 'Dashboard/dashboard.html')