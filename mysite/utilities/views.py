from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Utility
from .forms import UserForm


def index(request):
    return HttpResponse("Nothing Here Yet.")


class UserFormView(View):
    form_class = UserForm
    template_name = "utilities/registration_form.html"

    # Gets form for user.
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Processes form data.
    def post(self, request):
        # Passes information from user to form.
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleans up data.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('utilities:index')
        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                utilities = Utility.objects.filter(user=request.user)
                return render(request, 'utilities/index.html', {'utilities', utilities})
            else:
                return render(request, 'utilities/login.html', {'error_message', 'Your account has been disabled'})
        else:
            return render(request, 'utilities/login.html', {'error_message': 'Invalid login'})
    return render(request, 'utilities/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'utilities/login.html', context)
