from django.contrib import admin
from .models import product,goods,register_user
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class register_userInline(admin.TabularInline):
    model = register_user
    can_delete = False
    verbose_name_plural = "register_user"
class UserAdmin(BaseUserAdmin):
    inlines = (register_userInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

class goodsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(goods,goodsAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','onlinedate']
    list_editable = ['price',]
    list_per_page = 10

admin.site.register(product,productAdmin)