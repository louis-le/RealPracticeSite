from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, UpdateProfile
from .models import Utility, Employee
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Base web-page user gets directed to. Will be redirected to login if user isn't logged in.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        return render(request, 'utilities/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('utilities:index')
            else:
                return render(request, 'utilities/login.html', {'error_message', 'Your account has been disabled.'})
        else:
            return render(request, 'utilities/login.html', {'error_message': 'Invalid login.'})
    return render(request, 'utilities/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'utilities/login.html', context)


def register_user(request):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        form = UserForm(request.POST or None)
        if form.is_valid() and request.user.employee.manager:
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.employee = Employee()
            user.employee.company = request.user.employee.company
            return render(request, 'utilities/index.html')
        context = {
            "form": form,
        }
        return render(request, 'utilities/register.html', context)


def users(request):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        return render(request, 'utilities/users.html',  {'users': User.objects.all(), })


def user_detail(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        form = UpdateProfile(request.POST or None)
        specified_user = get_object_or_404(User, pk=user_id)
        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=request.user)
            form.actual_user = request.user
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('update_profile_success'))
        return render(request, 'utilities/user_detail.html', {'specified_user': specified_user, 'form': form})


def utility_detail(request, utility_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        specified_utility = get_object_or_404(Utility, pk=utility_id)
        return render(request, 'utilities/utility_detail.html', {'specified_utility': specified_utility, })


def remove_user(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return render(request, 'utilities/users.html',  {'users': User.objects.all(), })


def set_manager(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        specified_user = get_object_or_404(User, pk=user_id)
        specified_user.employee.set_manager()
        specified_user.employee.save()
        return render(request, 'utilities/user_detail.html', {'specified_user': specified_user, })


def add_utility(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    elif request.user.employee.manager:
        specified_user = get_object_or_404(User, pk=user_id)
        return render(request, 'utilities/add_utility.html', {'specified_user': specified_user, })
    else:
        return render(request, 'utilities/index.html')


def adding_util(request, employee_id, utility_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    elif request.user.employee.manager:
        specified_user = get_object_or_404(Employee, pk=employee_id)
        utility = get_object_or_404(Utility, pk=utility_id)
        specified_user.company.utilities.add(utility)
        specified_user.save()
        return render(request, 'utilities/add_utility.html', {'specified_user': specified_user, })
    else:
        return render(request, 'utilities/index.html')