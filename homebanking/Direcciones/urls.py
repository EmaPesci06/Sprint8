from django.urls import  path, include
from rest_framework.routers import DefaultRouter

from Direcciones import views

router = DefaultRouter()
router.register(r'direcciones', views.DireccionesView)

urlpatterns = [path('', include(router.urls))]