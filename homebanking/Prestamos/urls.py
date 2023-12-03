from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Prestamos import views

router = DefaultRouter()
router.register(r'prestamos', views.PrestamosView)

urlpatterns = [path('', include(router.urls))]