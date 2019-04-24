from rest_framework import routers

from employees.views import EmployeeViewSet
from restaurants.views import RestaurantViewSet


router = routers.DefaultRouter()

router.register(r'restaurants', RestaurantViewSet)
router.register(r'employees', EmployeeViewSet)
