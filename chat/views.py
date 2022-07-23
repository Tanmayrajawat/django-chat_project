import json

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Room, Message
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'chat/home.html')

def room(request, room_name):
    username = request.GET.get('username')
 #   room_details = Room.objects.get(title=room_name)
    room_details=Room.objects.get(title=room_name)
    messages = Message.objects.filter(room=room_details)


    return render(request, 'chat/room.html', {
        'username' : username,
        'room_name' : room_name,
        'room_details' : room_details,

    })

def send(request):
    message= request.POST['message']
    room_id = request.POST['room_name']
    username = request.POST['username']

    new_message = Message.objects.create(  value=message, user= username, room = room_id)
    new_message.save()
    return HttpResponse(json.dumps({'status': 'Message sent  '}), content_type='application/json')
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    print(request.POST)
    if Room.objects.filter(title=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(title=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)

def getMessages(request, room_name):
    room_details = Room.objects.get(name=room_name)

    messages = Message.objects.filter(room = room_details.id)
    return JsonResponse({"messages":list(messages.values())} )
   # pass
   # return render(request, 'chat/checkview.html')
   #  Create your views here.
