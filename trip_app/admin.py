from django.contrib import admin

from trip_app.models import Trip, TripClone, TripDetail

# Register your models here.
class TripAdmin(admin.ModelAdmin):
    
    list_filter = ('user__username', 'position_start', 'position_end', 'date_start', 'date_end') 
    search_fields = ['name', 'user__username', 'position_start', 'position_end', 'date_start', 'date_end']

    readonly_fields = ["user"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
    
class TripDetailAdmin(admin.ModelAdmin):
    
    list_filter = ('trip__name', 'trip__user__username', 'chkIn', 'date', 'budget', 'place__name') 
    search_fields = ['trip__name', 'trip__user__username', 'chkIn', 'date', 'budget', 'place__name']
    
admin.site.register(Trip, TripAdmin)
admin.site.register(TripDetail, TripDetailAdmin)
admin.site.register(TripClone)