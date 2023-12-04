# myapp/admin.py

from django.contrib import admin
from .models import *

admin.site.register(Login)
admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Enrollment)
admin.site.register(Material)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Grade)
admin.site.register(InteractionHistory)
admin.site.register(ReadingState)

