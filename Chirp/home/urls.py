from django.urls import path
from .views import *

urlpatterns = [
    path('', getAllChirps, name='home'),
    path('signup/', signup, name='Signup'),
    path('login/', loginView, name='Login'),
    path('logout/', logoutView, name='Logout'),
    path('about/', about, name='About'),
    path('contact/', contact, name='Contact'),
    path('chirp/', addChirp, name='Chirp')
]