from django.shortcuts import redirect,render
from .forms import MyRegisterForm
from .models import RegisterForm
# Create your views here.
def home(request):        
    if(request.method =='POST'):
        form = MyRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            
            return redirect('profile')
    form = MyRegisterForm()
    return render(request, 'home.html', {'form': form})

def profile(request):
    # form = MyRegisterForm()
    data = RegisterForm.objects.all()
    # print(data)
    return render(request, 'profile.html', {'datas': data})

def register(request):
    print(request.POST)
    if(request.method =='POST'):
        form = MyRegisterForm(request.POST, instance = RegisterForm)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        return redirect('home')

def delete(request, id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    return redirect('profile')

def update(request, id):
    data = RegisterForm.objects.get(id=id)
    form = MyRegisterForm()
    print(request.POST)
    # form.name = data.name
    # form.age = data.age
    # form.address = data.address
    # form.contact = data.contact
    # form.email = data.email
    return render(request, 'home.html', {'form': form})
    # name = request.name
    # age = request.age
    # address = request.address
    # contact = request.contact
    # email = request.email



