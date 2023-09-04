from django.contrib import admin
from payment_app.models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ('payment_status', 'payment_date', 'upload_img') 
    search_fields = ['customer__username',]
    
    # readonly_fields = ["payment_status"]    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(PaymentAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            if obj: # editing an existing object
                return ["payment_status"]
        return []
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(customer=request.user).filter(payment_status=False)
            queryset = queryset.filter(customer=request.user).filter(payment_status=False)
        return queryset

    # def save_model(self, request, obj, form, change):
    #     obj.customer = request.user
    #     return super().save_model(request, obj, form, change)

admin.site.register(Payment, PaymentAdmin)