from django.contrib import admin

from user_app.models import AccountDetail
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class AccountInline(admin.StackedInline):
    model = AccountDetail
    can_delete = False
    verbose_name_plural = 'AccountDetail'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset
    
class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)


admin.site.site_header = 'Plantrip | Administration'
admin.site.site_title  = 'Plantrip | Administration'
admin.site.index_title   = 'Hi, have a nice day!.'