from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Sucursales import views

router = DefaultRouter()
router.register(r'sucursales', views.SucursalView)

urlpatterns = [path('', include(router.urls))]