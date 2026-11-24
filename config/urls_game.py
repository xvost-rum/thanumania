from django.urls import path
from django.http import HttpResponse

def game_home(request):
    return HttpResponse("Game works!")
    
urlpatterns = [
    path('', game_home),
]