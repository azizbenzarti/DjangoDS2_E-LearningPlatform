from .models import *
from rest_framework import viewsets
from.serializers import *

# l crud :

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    #l cruds lkol

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    http_method_names=['GET','POST','PUT',] #mayaamalch delete
