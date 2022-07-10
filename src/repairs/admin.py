from django.contrib import admin

from .models import Repair, Device, Part, Solution, Step

# Register your models here.
admin.site.register(Device)
admin.site.register(Part)
admin.site.register(Solution)
admin.site.register(Step)
admin.site.register(Repair)