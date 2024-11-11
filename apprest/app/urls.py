from .api import CompanyViewSet, RoleViewSet, SessionViewSet, UserViewSet
from rest_framework import routers
router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')
router.register('api/roles', RoleViewSet, 'roles')
router.register('api/companies', CompanyViewSet, 'companies')
router.register('api/sessions', SessionViewSet, 'sessions')

urlpatterns = router.urls