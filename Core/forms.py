from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from Core.models import Room, User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter Room Name'}),
            'description': Textarea(attrs={'placeholder': 'Enter Room Description'}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'full_name', 'email', 'username', 'bio']


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'username', 'password1', 'password2']
