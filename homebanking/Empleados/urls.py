from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Empleados import views

router = DefaultRouter()
router.register(r'empleados', views.EmpleadosView)

urlpatterns = [path('', include(router.urls))]