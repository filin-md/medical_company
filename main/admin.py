from django.contrib import admin

from main.models import Analysis, Doctor, Order


# Register your models here.


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'price',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profile', 'experience', 'start_price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'consultation_date', 'client', 'phone',)