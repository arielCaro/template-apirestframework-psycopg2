from .models import user, role, company, session
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, RoleSerializer, CompanySerializer, SessionSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = user.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = role.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = session.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SessionSerializer


