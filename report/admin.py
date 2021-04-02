from django.contrib import admin


from .models import *

admin.site.register(Inspection)
admin.site.register(Operation)
admin.site.register(Blade)











# Register your models here.
# class TurbineResource(resources.ModelResource):

#     class Meta:
#         model = Turbines

# class InspectionImageAdmin(admin.StackedInline):
#     model = InspectionImage

# @admin.register(Inspection)
# class InspectionAdmin(admin.ModelAdmin):
#     inlines = [InspectionImageAdmin]

#     class Meta:
#        model = Inspection

# @admin.register(InspectionImage)
# class InspectionImageAdmin(admin.ModelAdmin):
#     pass