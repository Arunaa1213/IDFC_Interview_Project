from django.shortcuts import get_object_or_404, redirect, render
from .forms import MyRegisterForm
from .models import RegisterForm
from django.http import JsonResponse

# def home(request):        
#     if request.method == 'POST':
#         form = MyRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = MyRegisterForm()
#     return render(request, 'home.html', {'form': form})

def home(request):        
    if request.POST.get('requestType') == 'insert':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'redirect_url': 'profile'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = MyRegisterForm()
    return render(request, 'home.html', {'form': form})

def profile(request):
    datas = RegisterForm.objects.all()
    form = MyRegisterForm()
    return render(request, 'profile.html', {'datas': datas, 'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = MyRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         return redirect('home')

def delete(request, id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    return redirect('profile')

def update(request, id):
    data = RegisterForm.objects.get(id=id)
    if request.POST.get('requestType') == 'update':
        form = MyRegisterForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            # return redirect('profile')
            return JsonResponse({'redirect_url': '/profile'}, status=200)
    else:
        form = MyRegisterForm(instance=data)
    return render(request, 'profile.html', {'form': form, 'datas': RegisterForm.objects.all()})