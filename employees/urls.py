from rest_framework import routers
from .views import EmployeeViewSet,CongeViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'conges', CongeViewSet, basename='conge')

urlpatterns = router.urls
