from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateform
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account was created succesfully')
            return redirect('blogApp_index')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form,'bootstrap':'yes'})
@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateform()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile.html',context)
