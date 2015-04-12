from django.contrib import admin
from .models import USERS,TRIP,TASK,TASK_STATUS,TRIP_STATUS

admin.site.register(TASK)
admin.site.register(TRIP)
admin.site.register(USERS)
admin.site.register(TASK_STATUS)
admin.site.register(TRIP_STATUS)
