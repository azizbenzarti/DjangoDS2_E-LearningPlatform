
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('elearning_app/',include('elearning_app.urls')),
    path('user_authentification/',include('user_authentification.urls')),
]
