# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập tự động sau khi đăng ký
            return redirect('home')  # Thay bằng tên url trang chủ của bạn
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username hoặc mật khẩu không đúng.')
        else:
            messages.error(request, 'Dữ liệu không hợp lệ.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
@login_required
def account_view(request):
    user = request.user
    return render(request, 'users/account.html', {'user': user})

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserUpdateForm

@login_required
def update_account_view(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thông tin của bạn đã được cập nhật.')
            return redirect('users:account')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'users/update_account.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')

