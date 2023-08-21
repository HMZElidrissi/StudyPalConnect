from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Core.models import Room, Topic
from Core.forms import RoomForm


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "here's no user with this username")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "wrong password")

    return render(request, 'Core/login_register.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(host__username__icontains=q) |
        Q(description__icontains=q) |
        Q(name__icontains=q)
    )
    rooms_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'rooms_count': rooms_count}
    return render(request, 'Core/home.html', context)


def room(request, pk):
    selected_room = Room.objects.get(id=pk)
    context = {'selected_room': selected_room}
    return render(request, 'Core/room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'Core/room_form.html', context)


def update_room(request, pk):
    selected_room = Room.objects.get(id=pk)
    form = RoomForm(instance=selected_room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=selected_room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'Core/room_form.html', context)


def delete_room(request, pk):
    room_to_delete = Room.objects.get(id=pk)
    if request.method == 'POST':
        room_to_delete.delete()
        return redirect('home')
    return render(request, 'Core/confirm_delete.html', {'obj': room_to_delete})
