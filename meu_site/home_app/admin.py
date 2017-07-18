from django.contrib import admin
from .models import CustomUser
from dadosGeraisApp.admin import UsuarioModelAdmin
# Register your models here.

admin.site.register(CustomUser, UsuarioModelAdmin)