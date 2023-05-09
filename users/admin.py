from django.contrib import admin

from .models import User

admin.site.register(User)

# class UserCartInline(admin.TabularInline):
#     model = Cart
#     extra = 1
#
#
# class UserAdmin(admin.ModelAdmin):
#     inlines = (UserCartInline, )
#
#
# admin.site.register(Cart)
# admin.site.register(User, UserAdmin)
