from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *
# from .views import *

# Create your views here.
def getAllChirps(request):
    chirps = ChirpModel.objects.select_related('user')
    return render(request, 'home.html', {'chirps': chirps, 'user': request.user})

def signup(request):
    if(request.method == 'POST'):
        myUser = UserModel.objects.create_user(request)
        login(request, myUser)
        print("successfully Logged In")
        return redirect(getAllChirps)
    else:
        # form = UserForm()
        return render(request, 'signup.html')
    
def loginView(request):
    try:
        if(request.method == 'POST'):
            data = request.POST
            user = UserModel.objects.authenticate(username=data['username'], password=data['password'])
            if user is not None:                
                login(request, user)
                print("successfully Logged In")
            else:
                raise ValueError("Wrong Credentials")
            return redirect(getAllChirps)
        
        else:
            return render(request, 'login.html')
    except Exception as e:
        print(e)
        return render(request, 'login.html', {'error': e});

def addChirp(request):
    try:
        if(request.method == 'POST'):
            content = request.POST['content']
            if content is None or content == '':
                raise ValueError("No Content Given")
            ChirpModel.objects.create(user=request.user, content=content, image=request.FILES.get('image', None))
            return redirect(getAllChirps)
        else:
            return render(request, 'addChirp.html')
    except Exception as e:
        return render(request, 'addChirp.html', {'error': e})

def logoutView(request):
    logout(request)
    return redirect(getAllChirps)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')