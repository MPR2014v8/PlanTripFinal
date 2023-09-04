from django.contrib import admin
from businessplace_app.models import *

# Register your models here.


class BusinessPlaceAdmin(admin.ModelAdmin):

    readonly_fields = ["place_user"]
    
    list_filter = ('place_user__username', 'type__name', 'district', 'minPrice', 'maxPrice') 
    search_fields = ['name', 'place_user__username', 'type__name', 'district']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(place_user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.place_user = request.user
        return super().save_model(request, obj, form, change)


class BusinessPlacePictureAdmin(admin.ModelAdmin):

    readonly_fields = ["user"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


class VirtualTourAdmin(admin.ModelAdmin):

    readonly_fields = ["user"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


class RatingAndCommentAdmin(admin.ModelAdmin):

    readonly_fields = ["user"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
    
# class checkInLocationPlaceAdmin(admin.ModelAdmin):

#     readonly_fields = ["user"]

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:
#             queryset = queryset.filter(user=request.user)
#         return queryset

#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         return super().save_model(request, obj, form, change)
    



admin.site.register(BusinessPlace, BusinessPlaceAdmin)
admin.site.register(BusinessType)
admin.site.register(BusinessPlacePicture, BusinessPlacePictureAdmin)
admin.site.register(VirtualTour, VirtualTourAdmin)
admin.site.register(RatingAndComment, RatingAndCommentAdmin)
# admin.site.register(checkInLocationPlace, checkInLocationPlaceAdmin)
