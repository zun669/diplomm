from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'get_age', 'gender', 'diagnosis', 'attending_doctor')
    search_fields = ('full_name',)
    list_filter = ('attending_doctor',)