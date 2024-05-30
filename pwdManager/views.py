from django.shortcuts import render, redirect
from pwdManager.forms import CreateUserForm, PasswordForm
from pwdManager.models import PasswordEntry


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'registerform':form}
    
    return render(request, 'registration/signup.html', context=context)


def all_passwords(request):
    user = request.user
    if user.is_authenticated:
        entry_list = PasswordEntry.objects.filter(user=user)
        service_name = request.GET.get('service_name')
        if service_name:
            entry_list = entry_list.filter(service_name__icontains=service_name, user=user)
    else:
        entry_list = []
    return render(request, 'passwordlist.html', {'entry_list': entry_list})


def create_password_entry(request):
    form = PasswordForm()

    if request.method == 'POST':
        user = request.user
        data = request.POST.copy()
        data['user'] = user
        form = PasswordForm(data)
        print(request.POST)

        if form.is_valid():
            form.save()
            return redirect('passwordlist')
    
    context = {'newentry':form}
    return render(request, 'newentry.html', context=context)


def update_password_entry(request, entry_id):
    entry = PasswordEntry.objects.get(pk=entry_id)
    form = PasswordForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('passwordlist')
    return render(request, 'updateentry.html', {'entry':entry, 'form':form})


def delete_password_entry(request, entry_id):
    entry = PasswordEntry.objects.get(pk=entry_id)
    entry.delete()
    return redirect('passwordlist')
