from django.contrib import admin
from .models import Cliente

# Unregister the existing ClienteAdmin
admin.site.register(Cliente)