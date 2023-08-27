from django.contrib import admin

from Core.models import User, Room, Topic, Message

# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
