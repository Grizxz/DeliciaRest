from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("")
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)


