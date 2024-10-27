from django.shortcuts import render, redirect, get_object_or_404
from .models import VirtualUser
from .forms import VirtualUserForm
import time

def register_users(request):
    if request.method == 'POST':
        count = int(request.POST.get('count', 0))
        start_time = time.time()
        for i in range(count):
            username = f'virtual_user_{i}'
            email = f'user_{i}@example.com'
            VirtualUser.objects.create(username=username, email=email)
        end_time = time.time()
        duration = end_time - start_time
        return render(request, 'users/success.html', {'duration': duration})
    return render(request, 'users/register.html')

def list_users(request):
    users = VirtualUser.objects.all()
    return render(request, 'users/list.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(VirtualUser, id=user_id)
    user.delete()
    return redirect('list_users')

def user_detail(request, user_id):
    user = get_object_or_404(VirtualUser, id=user_id)
    return render(request, 'users/detail.html', {'user': user})