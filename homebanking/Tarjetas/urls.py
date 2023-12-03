from django import views
from django.urls import path, include
from Tarjetas import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tarjetas',views.TarjetaViewSet)

urlpatterns = [
    path('',include(router.urls))
]