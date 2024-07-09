from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, get_object_or_404
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Count
# from .views import *

# Create your views here.
def getAllChirps(request):
    chirps = ChirpModel.objects.annotate(totalLikes=Count('likes'))
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

def toggleLike(request):
    try:
        id = request.GET.get('id', None)
        if id is None or id == '':
            raise ValueError("No Id")
        
        chirp = ChirpModel.objects.get(id=id)
        try:
            like = LikeModel.objects.get(user=request.user, chirp=chirp)
        except Exception as e:
            like = False

        print(like)
        if like:
            like.delete()
            return JsonResponse({"success": True, "liked": False})
        else:
            LikeModel.objects.create(user=request.user, chirp=chirp)
            return JsonResponse({"success": True, "liked": True})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": e})

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
    
def getChirp(request, id):
    try:
        chirp = ChirpModel.objects.get(id=id)
        isLiked = get_object_or_404(LikeModel, chirp=chirp, user=request.user)
    except Exception as e:
        isLiked = 0

    return render(request, 'chirp.html', {"chirp": chirp, "isLiked": isLiked})

@login_required(login_url='/login/')
def addComment(request):
    try:
        content = request.POST.get('content', None)
        if content is None or content == '':
            raise ValueError("No Content")
        CommentModel.objects.create(content=content, user=request.user, chirp=ChirpModel.objects.get(id=request.POST.get('id', None)))
        return getChirp(request, id=request.POST.get('id', None))
    except Exception as e:
        print(e)
        return HttpResponse(e)
    

def getChatsPage(request):
    users = UserModel.objects.exclude(username=request.user.username)
    return render(request, 'chat.html', {'users': users})

def changeUsernameToUniqueID(room_name):
    uuid = 0

    for char in room_name:
        uuid = uuid + ord(char)
    print("uuid is: ", uuid)
    return uuid

def getChats(request, username):
    try:
        if username is None or username == '':
            raise ValueError("No Username")
        try:
            reciever = UserModel.objects.get(username=username)
            chats = ChatModel.objects.filter(models.Q(sender=request.user, reciever=reciever) | models.Q(sender=reciever, reciever=request.user)).order_by("dateTime")
        except Exception:
            chats = []

        chatsArr = []
        for chat in chats:
            chatsArr.append({'sender': chat.sender.username, 'reciever': chat.reciever.username, 'message': chat.message})

        room_name = changeUsernameToUniqueID(f'{request.user.username}{reciever.username}')

        return JsonResponse({"success": True, "chats": chatsArr, "room_name": room_name})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "error": e})

def logoutView(request):
    logout(request)
    return redirect(getAllChirps)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')