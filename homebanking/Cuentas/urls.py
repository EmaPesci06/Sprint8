from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Cuentas import views

router = DefaultRouter()
router.register(r'cuentas',views.CuentaViewSet)

urlpatterns = [
    path('',include(router.urls)),
]