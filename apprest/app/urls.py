from .api import CompanyViewSet, RoleViewSet, SessionViewSet, UserViewSet
from . import views 
from rest_framework import routers
router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')
router.register('api/roles', RoleViewSet, 'roles')
router.register('api/companies', CompanyViewSet, 'companies')
router.register('api/sessions', SessionViewSet, 'sessions')
router.register('api/Authentication', views.authentication, 'sessions')

urlpatterns = router.urls