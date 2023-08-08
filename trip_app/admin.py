from django.contrib import admin

from trip_app.models import Trip, TripDetail

# Register your models here.
class TripAdmin(admin.ModelAdmin):

    readonly_fields = ["user"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(Trip, TripAdmin)
admin.site.register(TripDetail)