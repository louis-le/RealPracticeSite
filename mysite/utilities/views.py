from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Utility, Employee


# Base web-page user gets directed to. Will be redirected to login if user isn't logged in.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        utilities = Utility.objects.filter(employee__id=request.user.employee.id)
        utilities = utilities.order_by(request.user.employee.get_utility_order_kywd())
        return render(request, 'utilities/index.html', {'utilities': utilities, })


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
                return render(request, 'utilities/login.html', {'error_message': 'Your account has been disabled.'})
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
    elif request.user.employee.manager:
        form = UserForm(request.POST or None)
        if form.is_valid() and request.user.employee.manager:
            user = form.save(commit=False)
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['confirm_password']
            if not password2:
                context = {
                    "form": form,
                    'error_message': "You must confirm your password",
                }
                return render(request, 'utilities/register.html', context)
            if password1 != password2:
                context = {
                    "form": form,
                    'error_message': "Your passwords do not match",
                }
                return render(request, 'utilities/register.html', context)
            user.set_password(password1)
            user.save()
            user.employee = Employee(user=user)
            user.employee.manager = False
            user.employee.company = request.user.employee.company
            user.employee.save()
            return redirect('utilities:index')
        context = {
            "form": form,
        }
        return render(request, 'utilities/register.html', context)
    else:
        return redirect('utilities:index')


def users(request):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        usrs = User.objects.filter(employee__company=request.user.employee.company)
        usrs = usrs.order_by(request.user.employee.get_user_order_kywd())
        return render(request, 'utilities/users.html',  {'users': usrs, })


def user_detail(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        specified_user = get_object_or_404(User, pk=user_id)
        return render(request, 'utilities/user_detail.html', {'specified_user': specified_user, })


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

        return redirect('utilities:users')


def disable_user(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        user = get_object_or_404(User, pk=user_id)
        user.is_active = False
        user.save()

        return redirect('utilities:users')


def enable_user(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        user = get_object_or_404(User, pk=user_id)
        user.is_active = True
        user.save()

        return redirect('utilities:users')


def set_manager(request, user_id):
    specified_user = get_object_or_404(User, pk=user_id)
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    elif request.user.employee.is_manager():
        specified_user.employee.set_manager()
        specified_user.employee.save()
    return redirect('utilities:user_detail', user_id=specified_user.id)


def add_utility(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    elif request.user.employee.manager:
        specified_user = get_object_or_404(User, pk=user_id)
        utilities = Utility.objects.filter(company=specified_user.employee.company).exclude(employee__id=specified_user.employee.id)
        return render(request, 'utilities/add_utility.html', {'specified_user': specified_user, 'utilities': utilities})
    else:
        redirect('utilities:index')


def adding_util(request, user_id, utility_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    elif request.user.employee.manager:
        specified_user = get_object_or_404(User, pk=user_id)
        utility = get_object_or_404(Utility, pk=utility_id)
        specified_user.employee.utilities.add(utility)
        specified_user.employee.save()
        return redirect('utilities:add_utility', user_id=specified_user.id)
    else:
        redirect('utilities:index')


def remove_utility(request, user_id, utility_id):
    if not request.user.is_authenticated():
        return render(request, 'utilities/login.html')
    else:
        specified_user = get_object_or_404(User, pk=user_id)
        utility = get_object_or_404(Utility, pk=utility_id)
        specified_user.employee.utilities.remove(utility)
        specified_user.employee.save()
        return redirect('utilities:index')


def username_sort(request):
    request.user.employee.adjust_user_sort_order(request.user.employee.ALPHA_SORT)
    return redirect('utilities:users')


def login_sort(request):
    request.user.employee.adjust_user_sort_order(request.user.employee.LOGIN_SORT)
    return redirect('utilities:users')


def joined_sort(request):
    request.user.employee.adjust_user_sort_order(request.user.employee.JOINED_SORT)
    return redirect('utilities:users')


def utility_sort(request):
    request.user.employee.adjust_utility_sort_order(request.user.employee.ALPHA_SORT)
    return redirect('utilities:index')

