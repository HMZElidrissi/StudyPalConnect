from django.shortcuts import render, redirect
from Core.models import Room
from Core.forms import RoomForm


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
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
