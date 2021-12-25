from enroll .models import User
from enroll.api.serializers import UserSerilizer
from rest_framework import serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerilizer