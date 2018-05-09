from django.contrib import admin
from issues.models import Task, Status, Place, Priority

# Register your models here.
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Place)
admin.site.register(Priority)

