from django.contrib import admin

from incidents.models import (
    Action, 
    Appointment, 
    Evaluation, 
    Implementation, 
    Job, 
    ProblemDefinition, 
    RootCause, 
    Solution, 
    SupportRequest,
)

admin.site.register(Action)
admin.site.register(Appointment)
admin.site.register(Evaluation)
admin.site.register(Implementation)
admin.site.register(Job)
admin.site.register(ProblemDefinition)
admin.site.register(RootCause)
admin.site.register(Solution)
admin.site.register(SupportRequest)