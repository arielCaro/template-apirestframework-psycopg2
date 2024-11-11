from .models import user, role, company, session
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, RoleSerializer, CompanySerializer, SessionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = role.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = session.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SessionSerializer