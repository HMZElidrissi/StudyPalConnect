from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Core.models import Room, Topic, Message
from Core.forms import RoomForm, UserForm


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    return render(request, 'Core/login_register.html', {'page': page})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'Core/login_register.html', {'form': form})


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
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {
        'rooms': rooms,
        'topics': topics,
        'rooms_count': rooms_count,
        'room_messages': room_messages
    }
    return render(request, 'Core/home.html', context)


def room(request, pk):
    selected_room = Room.objects.get(id=pk)
    # Many-to-One Relationship: object_set.all()
    # Many-to-Many Relationship: object.all()
    room_messages = selected_room.message_set.all()
    participants = selected_room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=selected_room,
            body=request.POST.get('body')
        )
        selected_room.participants.add(request.user)
        return redirect('room', pk=selected_room.id)

    context = {
        'selected_room': selected_room,
        'room_messages': room_messages,
        'participants': participants
    }

    return render(request, 'Core/room.html', context)


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        'user': user,
        'rooms': rooms,
        'room_messages': room_messages,
        'topics': topics
    }
    return render(request, 'Core/profile.html', context)


@login_required(login_url='/login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     new_room = form.save(commit=False)
        #     new_room.host = request.user
        #     new_room.save()
        return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, 'Core/room_form.html', context)


@login_required(login_url='/login')
def update_room(request, pk):
    selected_room = Room.objects.get(id=pk)
    topics = Topic.objects.all()

    if request.user != selected_room.host:
        return HttpResponse('You are not allowed here')

    form = RoomForm(instance=selected_room)
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        selected_room.topic = topic
        selected_room.name = request.POST.get('name')
        selected_room.description = request.POST.get('description')
        selected_room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'selected_room': selected_room}
    return render(request, 'Core/room_form.html', context)


@login_required(login_url='/login')
def delete_room(request, pk):
    room_to_delete = Room.objects.get(id=pk)

    if request.user != room_to_delete.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        room_to_delete.delete()
        return redirect('home')
    return render(request, 'Core/confirm_delete.html', {'obj': room_to_delete})


@login_required(login_url='/login')
def delete_message(request, pk):
    message_to_delete = Message.objects.get(id=pk)

    if request.user != message_to_delete.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        message_to_delete.delete()
        return redirect('home')
    return render(request, 'Core/confirm_delete.html', {'obj': message_to_delete})


@login_required(login_url='/login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    return render(request, 'Core/update_user.html', {'form': form})
