from django.urls import path
from .views import *

urlpatterns = [
    path('', getAllChirps, name='home'),
    path('signup/', signup, name='Signup'),
    path('login/', loginView, name='Login'),
    path('logout/', logoutView, name='Logout'),
    path('about/', about, name='About'),
    path('contact/', contact, name='Contact'),
    path('chirp/', addChirp, name='Chirp'),
    path('chirp/<int:id>', getChirp, name='getChirp'),
    path('comment/', addComment, name='comment'),
    path('like/', toggleLike, name='like'),
    path('chat/', getChatsPage, name='Chat'),
    path('chats/<str:username>', getChats, name='Chats'),
]