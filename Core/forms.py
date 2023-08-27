from django.forms import ModelForm, TextInput, Textarea
from Core.models import Room
from django.contrib.auth.models import User


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
        fields = ['email', 'username']
