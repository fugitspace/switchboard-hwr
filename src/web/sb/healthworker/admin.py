from django.contrib import admin
from sb.healthworker import models

class CadreAdmin(admin.ModelAdmin):
  list_display = ['title', 'created_at', 'updated_at']

admin.site.register(models.Cadre, CadreAdmin)
admin.site.register(models.District)
admin.site.register(models.DistrictType)
admin.site.register(models.Facility)
admin.site.register(models.FacilityType)
admin.site.register(models.HealthWorker)
admin.site.register(models.RegistrationNumber)
admin.site.register(models.Specialty)
